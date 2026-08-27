import chromadb
from chromadb.utils import embedding_functions

sentence_transformer=embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name='BAAI/bge-base-en-v1.5'
)

client=chromadb.PersistentClient(path="./store_db")
collection=client.get_collection(name='law_document',embedding_function=sentence_transformer)

query_text="What is the penalty for damaging a computer?"

results=collection.query(
    query_texts=[query_text],
    n_results=5
)
print(results)