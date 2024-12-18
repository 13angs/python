import json

with open('./product_list.json', 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)


def count_pv_items():
    pv_count = 0

    for product in json_data:
        if len(product['product_variant']) > 1:
            pv_count += 1

    print(pv_count)

def count_sku():
    sku_count = 0

    for product in json_data:
        for pv in product['product_variant']:
            if len(pv['sku']) > 0:
                sku_count += 1
    
    return sku_count