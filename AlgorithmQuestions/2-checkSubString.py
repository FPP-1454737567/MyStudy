"""
@Time  : 2024/2/21
@Author: panpan.fang@shopee.com
@File  : checkSubString.py
@IDE   : PyCharm
给定两个字符串 s和 t ，判断 s是否为 t 的子序列。
你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度n ~= 500,000），而 s 是个短字符串（长度 <=100）。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
"""


class Solution:
    def checkSubString(self, s: str, t: str) -> bool:
        k = 0
        result = True
        for i in range(len(s)):
            for j in range(k, len(t)):
                if s[i] == t[j]:
                    k = j + 1
                    result = True
                    break  # 只对当前的for循环有效
                else:
                    result = False
            if result is False: # 判断某一个字符找不到事时，即终止return
                return result
        return result


print(Solution().checkSubString("abc", "ahbgdc"))
print(Solution().checkSubString("axc", "ahbgdc"))
