import requests
import time
from decouple import config

API_TOKEN = config("API_TOKEN")

API_URL = "https://api.nextblackswan.com/api/v1/bentoweb/checkout/many"
body = {
    "action": "update_order",
    "shop_id": "9b959818c8454669845b10680c5760ed",
    "status_id": 4,
    "limit": 10,
    "provider_id": "9d68882715c24e71942e0a9d020fe963"
}

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"  # Assuming the API expects JSON
}

success_count = 0
while True:
    response = requests.put(url=API_URL, json=body, headers=headers)

    time.sleep(2)

    if response.status_code == 200:
        success_count += 1
        print(f"Successful request {success_count} made.")
        continue
    else:
        break