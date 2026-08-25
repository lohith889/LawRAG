import tiktoken
import re
encoder=tiktoken.get_encoding('cl100k_base')

def count_token(text:str) -> int:
    return len(encoder.encode(text))

def para_splitter(text:str) -> list[str]:
    para=re.split(
        r"(?<=[.!?])\s+(?=[A-Z(\[])",
        text.strip()
    )
    return[s for s in para]

def sentence_splitter(text:str) -> list[str]:
    sentences=re.split(
        r"\n\s*\n",
        text.strip()
    )
    return[s for s in sentences]