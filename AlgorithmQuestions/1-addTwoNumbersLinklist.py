"""
@Time  : 2024/2/20
@Author: panpan.fang@shopee.com
@File  : addTwonumbers.py
@IDE   : PyCharm
题目：两数相加
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""

class Solution:
    def addTwoNumbers(self, l1, l2):
        if len(l1) < len(l2):
            l1, l2 = l2, l1
        [l2.append(0) for i in range(len(l1) - len(l2))]
        revertl1 = list(l1)[::-1]
        revertl2 = list(l2)[::-1]
        numberl1 = ""
        numberl2 = ""
        for j in revertl1:
            numberl1 += str(j)
        for k in revertl2:
            numberl2 += str(k)
        print(numberl1, numberl2)
        l3 = int(numberl1) + int(numberl2)
        return [m for m in str(l3)[::-1]]


print(Solution().addTwoNumbers([2, 4, 3], [5, 6]))