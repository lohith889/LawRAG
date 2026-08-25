import tokenizer_utils
from typing import Any

MAX_TOKENS=350

def chunk_page(page:dict[str,Any],og_overlap:str)->tuple[list[dict[str,Any]],str]:
    text=page['text'].strip()

    if tokenizer_utils.count_token(text)<=MAX_TOKENS:
        return [{
            **page,
            "chunk_id":f"page_{page['page']:03d}_001",
            "chunk_text":text,
            "token_count":tokenizer_utils.count_token(text)
        }],tokenizer_utils.sentence_splitter(text)[-1]

    paras=tokenizer_utils.para_splitter(text)

    chunks=[]
    chunk_number=1
    current_token_count=0
    current_para=[]
    overlap=og_overlap 

    for para in paras:
        para_token=tokenizer_utils.count_token(para)
        if current_para and para_token + current_token_count>MAX_TOKENS:
            chunk_text=" ".join(current_para).strip()
            chunk_text=overlap+" "+chunk_text
            chunks.append({
                **page,
                "chunk_id":f"page_{page['page']:03d}_{chunk_number:03d}",
                "chunk_text":chunk_text,
                "token_count":current_token_count+tokenizer_utils.count_token(overlap)
            })
            overlap=current_para[-1]
            current_token_count=para_token
            chunk_number+=1
            current_para=[para]

        else:
            current_para.append(para)
            current_token_count+=para_token

    if current_para:
        chunk_text=" ".join(current_para)
        chunk_text=overlap+" "+chunk_text
        chunks.append({
            **page,
            "chunk_id":f"page_{page['page']:03d}_{chunk_number:03d}",
            "chunk_text":chunk_text,
            "token_count":current_token_count+tokenizer_utils.count_token(overlap)
        })

    og_overlap=tokenizer_utils.sentence_splitter(current_para[-1])[-1]
    return chunks,og_overlap
