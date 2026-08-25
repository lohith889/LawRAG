import json
from pathlib import Path
def save_json(data,output_path):
    Path(output_path).parent.mkdir(parents=True,exist_ok=True)

    with open(output_path,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=True,ensure_ascii=True)
        print("saved successfully")