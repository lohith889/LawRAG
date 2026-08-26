import chunker
import json
import save_json
import os

def chunk(path):
    with open(path,'r',encoding='utf-8') as f:
        doc=json.load(f)

    chunk=[]
    prev_overlap=""
    for page in doc:
        chunked,prev_overlap=chunker.chunk_page(page,prev_overlap)
        for x in chunked:
            chunk.append(x)
        
    return chunk


if __name__=='__main__':
    folder="D:\lohith\LawRAG\data\Parsed_Files"

    for item in os.listdir(folder):
        path=os.path.join(folder,item)

        chunks=chunk(path)

        output_path=os.path.join("D:\lohith\LawRAG\data\chunked_Files",item)
        save_json.save_json(chunks,output_path)
