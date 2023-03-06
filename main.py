import openai
from chat import chat
from whisper import voice_to_text
from voicevox import text_to_voice
from conf import APIKEY

openai.api_key = APIKEY

def main():
    messages = [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
    ]
    while True:
        text = voice_to_text()
        messages.append(
            {'role': 'user', 'content': text}
        )
        response = chat(messages)
        messages.append(
            {'role': 'assistant', 'content': response}
        )
        print(f'User   : {text}')
        print(f'ChatGPT: {response}')
        text_to_voice(response)


if __name__ == '__main__':
    main()
