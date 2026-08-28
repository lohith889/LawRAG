from query_retriever import retrival
from prompt_builder import build_prompt
from llm import llm_output

print("Law RAG - Type 'EXIT' to stop\n")

while True:
    query = input("Ask: ").strip()
    
    if query.upper() == 'EXIT':
        print("Goodbye!")
        break
    
    if not query:
        print("Please enter a question.\n")
        continue
    
    print("\n Searching...")
    context = retrival(query)
    prompt = build_prompt(query, context)
    
    print("Answer:\n")
    print(llm_output(prompt))