import chromadb 
import json



client=chromadb.PersistentClient(path="./store_db")
collection=client.get_or_create_collection(name="law_document")

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
