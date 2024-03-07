"""
@Time  : 2024/2/26
@Author: panpan.fang@shopee.com
@File  : 3-groupAnagrams.py
@IDE   : PyCharm
"""
# 题目：字母异位词分组
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list):
        d = defaultdict(list) #初始化一个defaultdict（默认字典），键是字符串类型，值是列表类型。defaultdict是一个Python内建字典类的子类，它重写了__missing__方法，当所访问的键不存在时，会调用指定的工厂函数生成一个默认值（这里是list[]）。
        for i in strs:
            d["".join(sorted(i))].append(i)
        return list(d.values())

    def groupAnagrams2(self, strs: list):
        # 定义一个字典，用于存储字母异位词分组结果
        anagram_dict = {}
        # 遍历所有单词
        for word in strs:
            # 将单词按照字母顺序排序，并作为键
            sorted_word = ''.join(sorted(word))
            # 如果该键已经在字典中，将当前单词加入到对应的列表中
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                # 如果该键不存在，则创建新的列表，并将当前单词加入其中
                anagram_dict[sorted_word] = [word]
        # 返回字典中所有值组成的列表，即为结果
        return list(anagram_dict.values())

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
