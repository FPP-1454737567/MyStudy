"""
@Time  : 2024/2/29
@Author: panpan.fang@shopee.com
@File  : 4-ProductExceptSelf.py
@IDE   : PyCharm
倒序：range(len(nums)-2, -1, -1)

"""
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
# 示例 1:
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
from functools import reduce


class Solution:
    # 虽然三种方法都能得出正确结果，但是只有第一种方法的时间复杂度是n
    def productExceptSelf1(self, nums: list) -> list:
        ans, tmp = [1] * len(nums), 1
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        # print(ans) #左下角
        for j in range(len(nums)-2, -1, -1):
            tmp *= nums[j+1]
            ans[j] *= tmp
        return ans

    def productExceptSelf2(self, nums: list) -> list:
        result = []
        v = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    v *= nums[j]
                else:
                    continue
            result.append(v)
            v = 1
        return result

    def productExceptSelf3(self, nums: list) -> list:
        result = []
        v = 1
        for i in range(len(nums)):
            k = nums[i]
            nums[i] = 1
            v = reduce(lambda x, y: x * y, nums)
            result.append(v)
            v = 1
            nums[i] = k
        return result

print(Solution().productExceptSelf1([1,2,3,4]))



