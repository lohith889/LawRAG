import re

def clean_text(text):
    text=re.sub(r"\n+","\n",text) #removes multiple \n
    text=re.sub(r"[ ]{2,}"," ",text) #removes multiple " "
    text=re.sub(r"\n\d+","",text) #removes page numbers
    text=re.sub(r"\f","",text)
    text= text.strip() #removes trailing and leading " "
    return text
