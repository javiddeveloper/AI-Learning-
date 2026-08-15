"""Session 5: Dataclass, Pydantic and SQLAlchemy models."""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field, field_validator
from sqlalchemy import DateTime, Enum as SAEnum, Numeric, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


PaymentStatusLiteral = Literal["pending", "completed", "failed", "refunded"]


# ============================================================
# 1. DATACLASS — domain/business model
# ============================================================

@dataclass
class Payment:
    """Payment object used by business logic."""

    id: int
    amount: Decimal
    currency: str
    status: PaymentStatusLiteral = "pending"
    description: str | None = None
    created_at: datetime | None = None

    def __post_init__(self) -> None:
        if self.created_at is None:
            self.created_at = datetime.now()

    def get_display_amount(self) -> str:
        return f"{self.amount:,.2f} {self.currency}"

    def is_payable(self) -> bool:
        return self.status in ("pending", "failed")

    def mark_as_completed(self) -> None:
        self.status = "completed"

    def mark_as_failed(self) -> None:
        self.status = "failed"


# ============================================================
# 2. PYDANTIC — API input/validation boundary
# ============================================================

class PaymentRequest(BaseModel):
    """Validated payment request received from an API client."""

    amount: Decimal = Field(
        gt=0,
        le=Decimal("1000000000"),
        description="Payment amount; maximum is 1 billion.",
    )
    currency: str = Field(
        min_length=3,
        max_length=3,
        description="Supported currency: IRR or USD.",
    )
    description: str | None = Field(default=None, max_length=200)

    @field_validator("currency")
    @classmethod
    def validate_currency(cls, value: str) -> str:
        value = value.upper()
        if value not in {"IRR", "USD"}:
            raise ValueError("currency must be IRR or USD")
        return value

    def to_payment(self, payment_id: int) -> Payment:
        return Payment(
            id=payment_id,
            amount=self.amount,
            currency=self.currency,
            status="pending",
            description=self.description,
        )


# ============================================================
# 3. SQLALCHEMY — persistence/database model
# ============================================================

class PaymentStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"


class Base(DeclarativeBase):
    pass


class PaymentModel(Base):
    """SQLAlchemy 2.x ORM model mapped to the payments table."""

    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), nullable=False)
    status: Mapped[PaymentStatus] = mapped_column(
        SAEnum(PaymentStatus),
        default=PaymentStatus.PENDING,
        nullable=False,
    )
    description: Mapped[str | None] = mapped_column(String(200), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )

    def __repr__(self) -> str:
        return (
            f"<PaymentModel(id={self.id}, amount={self.amount}, "
            f"currency={self.currency}, status={self.status.value})>"
        )

    @classmethod
    def from_payment(cls, payment: Payment) -> "PaymentModel":
        return cls(
            id=payment.id,
            amount=payment.amount,
            currency=payment.currency,
            status=PaymentStatus(payment.status),
            description=payment.description,
            created_at=payment.created_at,
        )

    def to_payment(self) -> Payment:
        return Payment(
            id=self.id,
            amount=self.amount,
            currency=self.currency,
            status=self.status.value,
            description=self.description,
            created_at=self.created_at,
        )
