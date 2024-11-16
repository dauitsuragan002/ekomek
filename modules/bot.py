import requests

from config import *

# Бот арқылы жауап алу
async def gpt_bot_response(user_prompt):
    
    headers = {
        "Authorization": f"Api-Key {API_KEY}",
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "text_prompt": user_prompt
    }

    url = f"{URL_KAZLLM}{ASSISTANT_ID}/interactions/"
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        bot_response = response.json()["vllm_response"]["content"]
        return bot_response
    else:
        print(f"Error fetching response: {response.status_code}")
        return "Қате: жауап алу мүмкін болмады."