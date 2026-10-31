from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Chunk:
    index: int
    content: str

def chunk_text(text: str, *, chunk_size_words: int = 100, overlap_words: int = 20) -> list[Chunk]:
    """Split text into overlapping word windows (word count is a tokenizer approximation)."""
    if chunk_size_words <= 0:
        raise ValueError("chunk_size_words must be greater than zero")
    if overlap_words < 0 or overlap_words >= chunk_size_words:
        raise ValueError("overlap_words must be >= 0 and smaller than chunk_size_words")
    words = text.split()
    if not words:
        return []
    step = chunk_size_words - overlap_words
    result: list[Chunk] = []
    for start in range(0, len(words), step):
        window = words[start:start + chunk_size_words]
        if not window:
            break
        result.append(Chunk(index=len(result), content=" ".join(window)))
        if start + chunk_size_words >= len(words):
            break
    return result
