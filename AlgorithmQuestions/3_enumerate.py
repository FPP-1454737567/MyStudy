"""
@Time  : 2024/2/26
@Author: panpan.fang@shopee.com
@File  : 3_enumerate.py
@IDE   : PyCharm
"""
import os.path
from collections import Counter


def test_enumerate():
    str = [4, 2, 7, 4, 4]
    str2 = "acbcdfe"
    str3={"a":1,"cd":40,"b":5}
    # for i, v in enumerate(str):
        # print(f"str[{i}] is:{v}")
        # print("str[{}] is:{}".format(i, v))
    print(str2)

    print(sorted(str2))
    freq_dict = Counter(str3)
    print(dict(freq_dict))


test_enumerate()
BASE_PATH = os.path.dirname(__file__)
path = os.path.join(BASE_PATH, "config", "data")
print(path)

