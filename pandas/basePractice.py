"""
@Time  : 2024/2/22
@Author: panpan.fang@shopee.com
@File  : basePractice.py
@IDE   : PyCharm
Data.loc[2]    # 得到 Data 的第二行
Data.[title2]    # 得到 Data 的第二列
文档：https://zhuanlan.zhihu.com/p/629715842
"""
import os.path
import pandas as pd

BASE_PATH = os.path.dirname(__file__)
filePath = BASE_PATH + "/data2.xlsx"
def basePractice():
    print("文件的绝对路径："+filePath)
    # sheet_name
    df = pd.read_excel(filePath, sheet_name=0) #sheet_name可为空，表示默认第一个sheet，0表示第一个sheet
    # print(type(df))
    print("-"*10+" 打印Dataframe详细信息：")
    print(df.info)
    print("-"*10+" 统计信息（最大值、最小值、中位数等等）")
    print(df.describe())
    # print(df.head())
    print("-"*10+" 遍历dataFrame,是行索引，r是每一行的值，是series类型")
    for i,r in df.iterrows():
        print(r)
        print(r["Hight"])
    print("打印r的类型："+str(type(r)))
    # 同时获取行数和列数：df.shape，输出元祖, 分别为行数和列数, 默认第一行是表头不算行数。
    print("行数："+str(df.shape[0]))
    print("列数："+str(df.shape[1]))
    print("-"*10+" 打印长度,此长度为行数:"+str(len(df)))
    print("-"*10+" 找出指定列：")
    print(df["Name"])
    print("-"*10+" 找出指定列：")
    print(df.loc[:, "Name"])
    print("-" * 10 + " 按索引和列标签找出指定行和列：")
    print(df.loc[1:2, "Name"])
    print("-" * 10 + " 注意iloc与loc的不同，按索引时，iloc相当于切片，不取最后一个")
    print("-" * 10 + " iloc按索引找出指定行和列：")
    print(df.iloc[0:2, 1:2])
    print("-" * 10 + " iloc找出指定行和列,起始索引和终止索引可为空：")
    print(df.iloc[1:2, :2])
    #判断Age为20的行，可以有多行
    cond = df['Age'] == 10
    # print(cond)
    # for key in df[cond]:
    #     print(key)
    for value in df[cond].values:
        print(value) #value是列表，匹配上的每一行数据
    # 用loc来定位具体元素，行是索引范围，列是tile的列表
    print("-"*10+" 按索引查找元素")
    print(df.loc[1:1, ["Name", "Age"]])
    print("-"*10+" 打印列名")
    print(df.columns.values)
    #根据条件查找
    print(df.loc[df['Age'] == 10, ])
    print(df.loc[df['Age'] < 20, ["Age","Hight"] ])
    print("-"*10+" 条件里的值如100不能加引号,列标签为空时表示列出所有的列")
    print(df.loc[(df['Age'] < 20) & (df["Hight"] == 100) & (df["Name"] == "alice"), ])
    print(df[df["Age"]>10])
    print("-"*10+" 导出数据：")
    df[df["Age"] > 10].to_excel(BASE_PATH + "/data3.xlsx")
basePractice()
