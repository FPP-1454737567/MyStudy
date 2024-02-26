"""
@Time  : 2024/2/5
@Author: panpan.fang@shopee.com
@File  : StringDivision.py
@IDE   : PyCharm
知识点：
字符串或者列表取第n个字符，都是用s[n]
判断大小写字母：s.isupper(),s.islower()
将字符串全变成大小写字母：s.upper(),s.lower()
切片：S4[:-1]，从0到倒数第一个数字，字符串和列表都由切片
每K个进行分割:S2K = [S2[j:j+K] for j in range(0,len(S2),K)]
求字符串中大写字母个数是countUppercase = sum(1 for n in S3[k] if n.isupper())
L.append：列表追加一个元素
" ".join(L):使用空格作为分割符，将L列表中的字符串相连接
L1.extend(L2): 两个列表相连接

"""
#题目
# 给定一个非空字符串S，其被N个‘-’分隔成N+1的子串，给定正整数K，要求除第一个子串外，其余的子串每K个字符组成新的子串，并用‘-’分隔。对于新组成的每一个子串，如果它含有的小写字母比大写字母多，则将这个子串的所有大写字母转换为小写字母；反之，如果它含有的大写字母比小写字母多，则将这个子串的所有小写字母转换为大写字母；大小写字母的数量相等时，不做转换。
# 输入描述:
# 输入为两行，第一行为参数K，第二行为字符串S。
# 输出描述:
# 输出转换后的字符串。
# 示例1
# 输入
# 3
# 12abc-abCABc-4aB@
# 输出
# 12abc-abc-ABC-4aB-@

import string

#解法1
class Test:
    def testString(self, K: int, S:string):
        L1 = S.split("-")
        S1 = ""
        for i in L1[1:]:
            S1 = S1 + i
        L2 = []
        S2 = ""
        for j in range(len(S1)):
            if (j+1) % K != 0:
                S2 = S2 + S1[j]
            else:
                S2 = S2 + S1[j]
                L2.append(S2)
                S2=""
        if S2:
            L2.append(S2)
        S4 = L1[0]+"-"
        for S3 in L2:
            lowerCaseCount = sum(1 for m in S3 if m.islower())
            upperCaseCount = sum(1 for m in S3 if m.isupper())
            if lowerCaseCount > upperCaseCount:
                S3= S3.lower()
            elif lowerCaseCount < upperCaseCount:
                S3= S3.upper()
            S4 = S4 + S3 + "-"
        print("S1 is:" + S1)
        print("S2 is:" + S2)
        print("L2 is:" + str(L2) )
        print("S3 is:" + S3)
        print("S4 is:" + S4)
        print("final result is : "+S4[0:-1])
# print("解法一： ")
# Test().testString(3, "12abc-abCABc-4aB@")



#解法2---------------------------------------------------------------------------------
class Solution:
    # 定义参数是int或者str类型，用冒号
    # def my_function(param: Union[int, str]):
    def stringDivision(self, K: int, S: string):
        #字符串分割
        S1 = S.split("-")
        #S2为将子串按K个字符分割后的
        S2 = ""
        #S3为所有分割后的子串，第一个子串不变
        S3 = []
        S3.append(S1[0])
        #后面的从第2个子串开始连起来
        for i in range(1, len(S1)):
            S2 = S2 + S1[i]
        #每K个进行分割
        S2K = [S2[j:j+K] for j in range(0,len(S2),K)]
        #将S3与S2K合并
        for j in S2K:
            S3.append(j)

        print("S2 is:"+S2)
        print("S2K is:")
        print(S2K)
        print("S3 is:")
        print(S3)
        #方法1
        countUppercase = 0
        countLowercase = 0
        # for k in range(1,len(S3)):
        #     for n in range(0,len(S3[k])):
        #         if S3[k][n].isupper():
        #             countUppercase = countUppercase+1
        #         elif  S3[k][n].islower():
        #             countLowercase = countLowercase+1
        #     if countUppercase>countLowercase:
        #         S3[k] = S3[k].upper()
        #     elif countUppercase < countLowercase:
        #         S3[k] = S3[k].lower()
        #     countUppercase = 0
        #     countLowercase = 0
        #方法2，列表推导式
        for k in range(1,len(S3)):
            countUppercase = sum(1 for n in S3[k] if n.isupper())
            countLowercase = sum(1 for n in S3[k] if n.islower())
            if countUppercase > countLowercase:
                S3[k] = S3[k].upper()
            elif countUppercase < countLowercase:
                S3[k] = S3[k].lower()

        S4 = ""
        for y in S3:
            S4 = S4 + y + "-"
        #用切片去除最后一个字符
        if S4[-1] == "-":
            print("the output is :" + S4[:-1])
        else:
            print("the output is :" + S4)
# print("解法二： ")
# Solution().stringDivision(3,"12abc-abCABc-4aB@")

#解法3
# k=int(input())
# h,s=input().strip().split('-',1)
# s=''.join(s.split('-'))
# for p in range(0,len(s),k):
#     if len([i for i in s[p:p+k] if 'a'<=i<='z'])>len([i for i in s[p:p+k] if 'A'<=i<='Z']):
#         h+='-'+s[p:p+k].lower()
#     elif len([i for i in s[p:p+k] if 'a'<=i<='z'])<len([i for i in s[p:p+k] if 'A'<=i<='Z']):
#         h+='-'+s[p:p+k].upper()
#     else:
#         h+='-'+s[p:p+k]
# print(h)

if __name__ == '__main__':
    print("解法一： ")
    Test().testString(3, "12abc-abCABc-4aB@")
    # print("解法二： ")
    # Solution().stringDivision(3, "12abc-abCABc-4aB@")