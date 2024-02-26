"""
@Time  : 2024/2/21
@Author: panpan.fang@shopee.com
@File  : httpApi.py
@IDE   : PyCharm
"""
import json

import requests


class HttpApi:
    def post(self):
        url = "https://http-gateway.spex.test.shopee.sg/sprpc/account.admin.change_user_status"
        payload = {
                    "status": 0,
                    "reason": "test",
                    "ban_bank_accounts": False,
                    "ar_trigger": False,
                    "userid": 1024730281,
                    "operator": "auto_data_script",
                    "region":"ID"
                  }
        header = {
            "x-sp-servicekey": "45318a86de2b7e59dec18a3bda5d5541",
            "x-sp-sdu": "account.admin.br.staging.master.default",
            "Content-Type": "application/json",
            "shopee-baggage": "CID=id"
        }
        res = requests.post(url=url, data=json.dumps(payload), headers=header)
        print(res.status_code)
        print(res.text)
        print(type(res.text))
        print(json.loads(res.text))
        print(type(json.loads(res.text)))

        print(res.cookies)
        print(res.headers)
        # print(json.load(res))

HttpApi().post()

