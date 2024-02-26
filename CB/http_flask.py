"""
@Author  :   林紫君
@Contact :   zijun.lin@shopee.com
@Software:   PyCharm
@File    :   http_flask.py
@Time    :   2022/7/28 2:06 PM
"""

import requests
from flask import Flask, request, jsonify, abort
import hmac
import time
import json
from concurrent.futures import ThreadPoolExecutor




app = Flask(__name__)

executor = ThreadPoolExecutor(2)

def encryption(data):
    obj = hmac.new(msg=data, digestmod=None)
    return obj.hexdigest()

@app.route('/gitlab_hook', methods=['GET','POST'])
def gitlab_hook():
    if request.method =='GEI':
        #can use time function to mock timeout,here is 0.2 second
        time.sleep(0.20)
        #can change the status code 200 to mock return error
        return jsonify({'status':'success'}),200

    elif request.method == "POST":

        #need to change to the url ur service called
        url = "https://logistics-api.test.shopee.tw/api/v3/logistics/address/"
        t_userid = 1201271022
        t_token = request.json['token'] #if u want to mock api failed, u can change the token to a wrong one
        create_row_data = {'user_id': int(t_userid),'token':str(t_token)}
        response = requests.post(
            url, data=json.dumps(create_row_data),
            headers={'Content-Type': 'application/json'}
        )

        response = response.text
        print(response)
        #can use time function to mock timeout,here is 0.2 second
        time.sleep(0.2)
        return response
    else:
        abort(402)


if __name__ == '__main__':
    app.run(host='127.0.0.1',port='6606')

