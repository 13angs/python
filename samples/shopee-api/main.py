import hmac
import json
import time
import requests
import hashlib

code = ""

def shop_auth():
    timest = int(time.time())
    host = "https://partner.test-stable.shopeemobile.com"
    path = '/api/v2/auth/token/get'
    partner_id = 123
    partner_key = "".encode()
    tmp_base_string = "%s%s%s" % (partner_id, path, timest)
    base_string = tmp_base_string.encode()
    sign = hmac.new(partner_key, base_string, hashlib.sha256).hexdigest()
    ##generate api
    url = host + path
    params = {
        "partner_id": partner_id,
        "timestamp": timest,
        "sign": sign,
        "code": code
    }
    response = requests.post(url=url, params=params)
    print(response.content)

shop_auth()