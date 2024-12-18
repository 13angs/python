import requests
from decouple import config
import json
import os
import math
import time


def fetch_product_list(store_id, limit=10, page=1):
    url = f"https://queue.bentoweb.com/api/productlist?limit={limit}&page={page}&is_backend=0&store_id={store_id}"

    token = config('API_TOKEN')

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}'
    }

    try:

        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f'An error occured: {e}')
        return None


def append_to_json_file(file_path, new_data):
    if os.path.exists(file_path):

        with open(file_path, 'r', encoding='utf-8') as json_file:
            existing_data = json.load(json_file)
    else:
        existing_data = []

    existing_data.extend(new_data)

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(existing_data, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    store_id = 47805

    init_product_list = fetch_product_list(store_id, limit=1, page=1)
    total_products = init_product_list['data']['total']

    limit = 20

    total_pages = math.ceil(total_products / limit)

    incremetal_page = 1

    while total_pages >= incremetal_page:
        product_list = fetch_product_list(store_id=store_id, limit=limit, page=incremetal_page)

        if product_list is not None:
            append_to_json_file('./product_list.json', product_list['data']['product_list'])

        incremetal_page += 1
        time.sleep(1)