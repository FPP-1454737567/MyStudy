from flask import abort, jsonify, Flask, request, Response

app = Flask(__name__)
# 增加配置，支持中文显示
app.config['JSON_AS_ASCII'] = False

tasks = {
    "header": {
        "seq_id": "11234167868686876876",
        "retcode": 0,
        "rettype": "",
        "message": ""
    },
    "can_reselect": True,
    "failure_reason": "reselect_expired---"
}

@app.route('/mock_test', methods=['GET','POST'])
def get_task():
    return jsonify(tasks)


if __name__ == '__main__':
    app.run(host = '127.0.0.1',port = 6868,debug = True)

# url:127.0.0.1:6868/mock_test