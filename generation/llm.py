def llm_output(prompt: str) -> str:
    
    from openai import OpenAI
    import os
    client = OpenAI(
        api_key=os.environ.get("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
    )

    response = client.responses.create(
        input=prompt,
        model="openai/gpt-oss-20b",
    )
    for item in response.output:
        if item.type == 'message':
            for content in item.content:
                if content.type == 'output_text':
                    return content.text