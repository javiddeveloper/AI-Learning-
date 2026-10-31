from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader


@dataclass(frozen=True, slots=True)
class ExtractedPage:
    page_number: int
    text: str


def extract_text_file(path: Path) -> list[ExtractedPage]:
    text = path.read_text(encoding="utf-8")
    return [ExtractedPage(page_number=1, text=text)]


def extract_pdf(path: Path) -> list[ExtractedPage]:
    reader = PdfReader(str(path))
    pages: list[ExtractedPage] = []

    for page_number, page in enumerate(reader.pages, start=1):
        pages.append(
            ExtractedPage(
                page_number=page_number,
                text=page.extract_text() or "",
            )
        )

    return pages


def parse_document(path: Path) -> list[ExtractedPage]:
    suffix = path.suffix.lower()

    if suffix == ".txt":
        return extract_text_file(path)
    if suffix == ".pdf":
        return extract_pdf(path)

    raise ValueError(f"Unsupported document type: {suffix}")
