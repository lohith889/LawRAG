import chromadb 
import json
from chromadb.utils import embedding_functions

model_path=r"D:\lohith\LawRAG\Save_model\Model_files"

embedding_fn=embedding_functions.SentenceTransformerEmbeddingFunction(model_path)

client=chromadb.PersistentClient(path="D:\lohith\LawRAG\database")
collection=client.get_or_create_collection(name="law_document",embedding_function=embedding_fn)

with open("D:\lohith\LawRAG\data\embedded_File\embedded.json",'r',encoding='utf-8') as f:
    doc=json.load(f)
    print("file loaded successfully")

id=[]
text=[]
emb=[]
for item in doc:
    id.append(item['chunk_id'])
    text.append(item['chunk_text'])
    emb.append(item['embeddings'])

collection.add(
    documents=text,
    embeddings=emb,
    ids=id
)
print("Document added to DB")
