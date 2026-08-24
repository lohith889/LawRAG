import pymupdf
import parser_utils
import save_json
import os

def text_extractor(path):
    doc=pymupdf.open(path)
    pages=[]
    for page_number,page in enumerate(doc):
        text=page.get_text()
        pages.append({
            "page":page_number+1,
            "text":text
        })
    doc.close()
    return pages

if __name__=="__main__":
    folder_path="D:\lohith\LawRAG\Raw file"
    for item in os.listdir(folder_path):
        pdf=os.path.join(folder_path,item)
        pages=text_extractor(pdf)
        for page in pages:
            page["text"]=parser_utils.clean_text(page["text"])

        output_folder="D:\lohith\LawRAG\Parsed_Files"
        iter=item+".json"
        output_path=os.path.join(output_folder,iter)
        save_json.save_json(pages,output_path)