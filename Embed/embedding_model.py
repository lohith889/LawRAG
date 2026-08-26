from sentence_transformers import SentenceTransformer
from typing import Any

MODEL_NAME="BAAI/bge-base-en-v1.5"
model=SentenceTransformer(MODEL_NAME)

def embed_model(file:dict[str,Any],source:str) -> dict[str,Any]:
    embeddings=model.encode(file["chunk_text"],normalize_embeddings=True)

    return {
        "chunk_id":file['chunk_id'],
        "embeddings":embeddings.tolist(),
        "chunk_text":file["chunk_text"],
        "token_count":file["token_count"],
        "source_pdf":source
        }

