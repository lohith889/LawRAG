from embedding_model import embed_model
import json
import os 
from pathlib import Path

def embedding(path,source):
    vector=[]
    with open(path,'r',encoding='utf-8') as f:
        doc=json.load(f)
        for chunk in doc:
            vector.append(embed_model(chunk,source))
    return vector

def save_json(data,path):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    print(path)
    with open(path,"w",encoding='utf-8') as f:
        json.dump(data,f,indent=True,ensure_ascii=True)
        print("saved successfully")

if __name__=="__main__":
    input_folder="D:/lohith/LawRAG/data/chunked_Files"
    output_folder=os.path.join("D:\lohith\LawRAG\data\embedded_File\embedded.json")
    emb=[]
    for item in os.listdir(input_folder):
        path=os.path.join(input_folder,item)
        emb.extend(embedding(path,item))

    save_json(emb,output_folder)
    