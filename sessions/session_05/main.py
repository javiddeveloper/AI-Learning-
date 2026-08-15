"""Session 5: API -> domain -> persistence model flow."""

from decimal import Decimal

from pydantic import ValidationError
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Base, PaymentModel, PaymentRequest


def main() -> None:
    # 1. API input -> Pydantic validation
    request_data = {
        "amount": "250000.00",
        "currency": "irr",
        "description": "Book purchase",
    }

    request = PaymentRequest.model_validate(request_data)
    print("Pydantic:", request)
    print("JSON:", request.model_dump_json())

    # 2. Pydantic -> domain dataclass
    payment = request.to_payment(payment_id=1001)
    print("\nDataclass:", payment)
    print("Display amount:", payment.get_display_amount())
    print("Is payable:", payment.is_payable())

    # Business logic changes domain state.
    payment.mark_as_completed()
    print("After completion:", payment.status)

    # 3. Domain dataclass -> SQLAlchemy ORM model
    payment_model = PaymentModel.from_payment(payment)
    print("\nORM model:", payment_model)

    # 4. ORM model -> SQLite persistence
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(payment_model)
        session.commit()

        saved_payment = session.scalar(
            select(PaymentModel).where(PaymentModel.id == 1001)
        )

        if saved_payment is None:
            raise RuntimeError("Payment was not found after persistence")

        restored_payment = saved_payment.to_payment()
        print("\nRestored domain object:", restored_payment)

    # 5. Runtime validation failure
    invalid_data = {
        "amount": Decimal("-1000"),
        "currency": "EUR",
    }

    try:
        PaymentRequest.model_validate(invalid_data)
    except ValidationError as exc:
        print("\nExpected validation error:")
        print(exc)


if __name__ == "__main__":
    main()
