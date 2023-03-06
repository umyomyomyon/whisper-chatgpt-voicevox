import openai

def chat(messages: list) -> str:
    result = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    response_text = result['choices'][0]['message']['content']
    return response_text
