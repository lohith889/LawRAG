import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

with open("D:/lohith/LawRAG/data/embedded_File/embedded.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

model = SentenceTransformer("BAAI/bge-base-en-v1.5")

query = "is knowingly creating, publishing or otherwise making available a digital signature certificate will be punished?"
query_emb = model.encode(query, normalize_embeddings=True)

similarities = []
for item in data:
    chunk_emb = np.array(item['embeddings'])
    sim = cosine_similarity([query_emb], [chunk_emb])[0][0]
    similarities.append((sim, item))

similarities.sort(key=lambda x: x[0], reverse=True)
print(f"Top 5 matches for: '{query}'")
for i, (score, item) in enumerate(similarities[:5], 1):
    print(f"{i}. Score: {score:.4f}")
    print(f"   Text: {item.get('chunk_text', '')[:100]}...")
    print()