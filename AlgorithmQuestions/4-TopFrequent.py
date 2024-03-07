"""
@Time  : 2024/2/27
@Author: panpan.fang@shopee.com
@File  : 4-TopFrequent.py
@IDE   : PyCharm
知识点：字符串、数组和列表有序；字典无序；
如果需要有序的键值对集合，应该使用collections.OrderedDict或者将键/值排序后再遍历字典。
count2 = sorted(dict(count1).items(), key=lambda item: item[1], reverse=True)
"""
# 题目：
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
# 示例 1:
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:
# 输入: nums = [4,1,-1,2,-1,2,3], k = 2
# 输出: [-1,2]
import collections
from functools import reduce


class Solution:
    def topKFrequent1(self, nums: list, k: int) -> list:
        '''
        方法一：collections.Counter，most_common()函数直接得出
        :param nums:
        :param k:
        :return:
        '''
        count = collections.Counter(nums)
        print(count)
        print(count.most_common(k))
        return [item[0] for item in count.most_common(k)]

    #
    def topKFrequent2(self, nums: list, k: int) -> list:
        '''
        方法二：collections.Counter，使用lambda函数、列表推导式、sort函数
        :param nums:
        :param k:
        :return:
        '''
        print(collections.Counter(nums))
        count1 = collections.Counter(nums)
        #此处用for循环遍历count中的key时，顺序会变
        # for v in count1:
        #     print(v)
        print(dict((count1).items()))
        #按照value排序：先将count1专成含有数组的列表，才能用lambda函数；item[1]是按照每个元组的第二个值进行排序，reverse倒序
        #最终sorted后返回一个排序后的含有数组的列表
        count2 = sorted(dict(count1).items(), key=lambda item: item[1], reverse=True)
        print(count2)
        #[K[0] for K in count2]： 取count2里的元组的第一个key，列表推导式组成新的列表
        #[0:k]使用切片取前k个
        return [K[0] for K in count2][0:k]


# print(Solution().topKFrequent2([3,0,1,0],1))
# print(Solution().topKFrequent2([4,1,-1,2,-1,2,3],2))