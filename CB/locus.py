"""
@Author  :   林紫君
@Contact :   zijun.lin@shopee.com
@Software:   PyCharm
@File    :   locus.py
@Time    :   2022/7/28 11:36 PM
"""
from locust import TaskSet, task, HttpUser
import datetime
i=1

class WebsiteTasks(TaskSet):

    @task
    def call_standardization(self):
        url = "/sprpc/account.bff.address.get_user_address_list?param=363249b7bccc5eda4bad87105f8661a7" #change the url to  http-gateway url u need to test
        #need to change the request, please remember to use type conversion functions
        req ={
           str("bff_meta"):{
               str("userid"):int(1207126418)
           }
        }
        #need to change the headers
        headers ={
            "x-sp-sdu": "account.core.global.test.master.default",
            "x-sp-servicekey": "8d3dbc642292cf01a04216bf494367e8"
        }
        # these part no need to change
        with self.client.post(url=url, json=req, headers=headers) as res:
            if res.status_code != 200:
                print(res.status_code)
                res.failure(res.status_code)
                return
            print(res.json())
            print(datetime.datetime.now().strftime("%H:%M:%S"))
            global i
            i = i +1
            print(i)



class WebsiteUser(HttpUser):
    tasks = [WebsiteTasks]
    host = "https://http-gateway.spex.test.shopee.sg"
    min_wait = 1000
    max_wait = 5000
