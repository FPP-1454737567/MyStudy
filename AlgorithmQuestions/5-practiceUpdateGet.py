"""
@Time  : 2024/2/29
@Author: panpan.fang@shopee.com
@File  : 5-practiceUpdateGet.py
@IDE   : PyCharm
"""
test_request = {
    "test":{
        "a":1,
        "b":2
    },
    "staging": {
        "a": 11,
        "b": 22
    },
}
test_template = {
    "test": {
        "a": "1a",
        "b": 2
    },
    "live": {
        "a": 111,
        "b": 222
    },
}
# req = test_request.get("staging", None)
# print(req)
# test_request.update(test_template)
# print(test_request)
# print(test_template)
print(test_template.keys())
for i in test_template.keys():
    print(i)