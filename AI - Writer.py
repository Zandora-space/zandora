import os
import openai

openai.api_key = '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'

prompt=input("Ask a Question: ")


def write():
    response=openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=250,
    temperature=0.4
    )
    result=response['choices'][0]['text']
    print(result)
    
write()