import os

import pyperclip
from openai import OpenAI


def _get_client():
    return OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=os.getenv('OPEN_API_KEY'),
    )

def _get_response(client, user_content: str, system_context: str = "You are a data scientist"):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "system", "content": "You are data scientist"},
            { "role": "user", "content": user_content}
        ],
        model="gpt-3.5-turbo",
    )
    
    response = chat_completion.choices[0].message.content
    pyperclip.copy(response)
    return response

def _prompt_generator():
    pass