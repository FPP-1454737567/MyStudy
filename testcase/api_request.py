"""
@Time  : 2023/7/13
@Author: panpan.fang@shopee.com
@File  : api_request.py
@IDE   : PyCharm
"""
import json

import requests
headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
data1 = {
    "env": "staging",
    "country": "id",
    "username": "androidautouser20230321kizv",
    "password": "Password"
}
loginUrl = "http://127.0.0.1:1002/sc/seller_center/login_seller_center/"
draftUrl = "http://127.0.0.1:1002/sc/decoration/draft_publish_create/"
data2 = {
    "env": "staging",
    "country": "id",
    "draft_id": 2452,
    "publish_mode": 1
}

if __name__ == '__main__':
    response1 = requests.post(loginUrl, json.dumps(data1), headers=headers)
    response2 = requests.post(draftUrl, json.dumps(data2), headers=headers)
    print("response1:"+ response1.text)
    print("response2:"+ response2.text)