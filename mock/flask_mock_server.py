import json

from flask import abort, jsonify, Flask, request, Response

app = Flask(__name__)
# 增加配置，支持中文显示
app.config['JSON_AS_ASCII'] = False

# 方式1：直接定义mock的数据
# tasks = {
#     "header": {
#         "seq_id": "11234167868686876876",
#         "retcode": 0,
#     },
#     "can_reselect": True,
#     "failure_reason": "reselect_expired---"
# }

# 方式2：从文件中读取，注意是load不是loads
with open("./mock_data.json", "r") as data:
    tasks = json.load(data)


@app.route('/mock_test', methods=['GET', 'POST'])
def get_task():
    return jsonify(tasks)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6868, debug=True)

# curl 127.0.0.1:6868/mock_test
