"""
@Time  : 2024/2/21
@Author: panpan.fang@shopee.com
@File  : initPath.py
@IDE   : PyCharm
"""
import os
# __file__ 当前文件名
print(os.path.abspath(__file__))  # 当前文件的路径及名称
print(os.path.dirname(__file__))  # 当前文件的路径
print(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的目录路径
print(os.path.dirname(os.path.dirname(__file__)))  # 当前文件的目录路径
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 当前文件的目录路径

# get project dir
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(BASEDIR)
