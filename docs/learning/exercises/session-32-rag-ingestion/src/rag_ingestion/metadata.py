from dataclasses import dataclass
from uuid import UUID, uuid5

_NAMESPACE = UUID("7e4b4c36-f76b-4d53-9e89-7c56c33c9d11")

@dataclass(frozen=True, slots=True)
class ChunkMetadata:
    document_id: str
    chunk_id: str
    source_name: str
    page_number: int
    chunk_index: int
    content_hash: str

def build_chunk_metadata(*, document_id: str, source_name: str, page_number: int,
                         chunk_index: int, content_hash: str) -> ChunkMetadata:
    chunk_id = uuid5(_NAMESPACE, f"{document_id}:{content_hash}:{page_number}:{chunk_index}")
    return ChunkMetadata(document_id, str(chunk_id), source_name, page_number, chunk_index, content_hash)
