# import cv2
# import numpy as np
# from pyspark import SparkConf, SparkContext
# # class momery:
# #
# #     def __init__(self,name,age,place):
# #         self.name = name
# #         self.age = age
# #         self.place = place
# #
# #     def __str__(self):
# #         return f"你的名字：{self.name} 年龄为{self.age}来自 {self.place}"
# #
# # class Read_data:#定义一个抽象类
# #
# #     def read_data(self):
# #         pass
# #
# # class My_read(Read_data):   #在子类中实现父类的方法，读取data.txt中的数据
# #
# #     def __init__(self ,path):
# #         self.path = path
# #
# #     def read_data(self) ->momery:
# #         f = open(self.path ,"r" ,encoding="utf-8")
# #         record_list :list[momery] =  []
# #
# #         for line in f.readlines():
# #             line = line.strip()
# #             data_line = line.split("，")
# #             record = momery(data_line[0],data_line[1],data_line[2])
# #             record_list.append(record)
# #
# #         f.close()
# #         return record_list
# #
# # if __name__ == "__main__":
# #     filed = My_read('data.txt')
# #     file_data : list= filed.read_data()
# #     for l in file_data:
# #         print(l)
# # print(cv2.__version__)#测试cv2是否安装成功，如果成功返回一个版本号
#
# # conf = SparkConf().setMaster('local').setAppName('test')
# #
# # sc = SparkContext(conf=conf)
# #
# # rdd = sc.textFile("文件路径")
# # rdd1 = sc.parallelize([1,2,3,4,5])
# # print(rdd1.collect())
# # print(sc.version)
# #
# # sc.stop()
#
# # class Solution(object):
# #     def myAtoi(self, s):
# #         """
# #         :type s: str
# #         :rtype: int
# #         """
# #         s = s.strip()
# #         print(s)
# #         if s =="" or (len(s) == 1 and s[0]=='-'or len(s)==1 and s[0]=="+"):
# #             return 0
# #         if 'a'<=s[0]<='z' or s[0] == '0' and not('0' <= s[1] <= '9') or s[0]=='+' and s[1] =='-' or [0]=='-' and s[1] =='+':
# #             return 0
# #         num = 0
# #         flag = 0
# #         zero = 1
# #         if s[0] =='-':
# #             flag = 1
# #             s = s[1:]
# #         elif s[0]=='+':
# #             s = s[1:]
# #         for char in s:
# #             if '0' <= char <='9':
# #                 if char =='0' and zero:
# #                     continue
# #                 elif '0' <= char <='9' and flag:
# #                     num = num * 10 - int(char)
# #                     if num < (-2 **31) -1:
# #                         num = (-2 **31)
# #                         break
# #                     zero = 0
# #                 elif '0' <= char <='9':
# #                     num = num*10 + int(char)
# #                     if num > 2 **31 -1:
# #                         num = 2 **31
# #                         num -=1
# #                         break
# #                     zero = 0
# #             else:
# #                 break
# #
# #         return num
# # st = Solution()
# # num = st.myAtoi('00000-42')
# # print(num)
# #方法一：
# # class Solution(object):
# #     def findMedianSortedArrays(self, nums1, nums2):
# #         """
# #         :type nums1: List[int]
# #         :type nums2: List[int]
# #         :rtype: float
# #         """
# #         last_num = []
# #         size1,size2 = len(nums1) ,len(nums2)
# #         current1,current2 = 0,0
# #
# #手动排序
# #         while current1 < size1 and current2 < size2:
# #             if nums1[current1] <= nums2[current2]:
# #                 last_num.append(nums1[current1])
# #                 current1+=1
# #             else:
# #                 last_num.append(nums2[current2])
# #                 current2 +=1
# #
# #         if current1 >= size1:
# #             last_num.extend(nums2[current2 : ])
# #         elif current2 >=size2:
# #             last_num.extend(nums1[current1 : ])
# #         size = len(last_num)
# #         print(last_num)
# #         current = 0
# #         if not(size % 2):
# #             current = (last_num[((size/2) - 1)]+last_num[size/2])/2.0
# #         else :
# #             current = last_num[size/2]
# #         return current
# #方法二：
#
# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         last_num = nums1+nums2
#         last_num.sort()             #利用python中的函数自动排序
#
#         size = len(last_num)
#
#         if not(size % 2):
#             return (last_num[size/2 - 1]+last_num[size/2])/2.0
#         else :
#             return last_num[size/2]
#
# st = Solution()
# data = st.findMedianSortedArrays([1,3],[2])
# class Solution(object):
#     def rotate(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
#         num = [[0]*len(matrix)]*len(matrix)
#         i,j=0,len(matrix)
#         while i < j:
#             x = 0
#             while x < j:
#                 num[i][x] = matrix[j - x - 1][i]
#                 print(f"num[{i}][{x}] = matrix[{j-x-1}][{i}]")
#                 x += 1
#             i += 1
#         num[:] = matrix
# st = Solution()
# s = [[1,2,3],[4,5,6],[7,8,9]]
# st.rotate(s)
# print(s)



#方法一，暴力搜索  会超时
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         mx = 0
#         size = len(prices)
#         for x in range(0,size-1):
#             #判断取当前的股票是否可以有盈利
#             if  max(prices[x+1:]) - prices[x] > 0:
#                 #判断出最大的收益值
#                 if max(prices[x+1:]) - prices[x] > mx:
#                     mx =max(prices[x+1:]) - prices[x]
#         return mx
#方法二
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_price=min_price=prices[0]
#         res=0
#         for price in prices:
#             if price>max_price:
#                 max_price=price
#                 res=max(res,max_price-min_price)
#             if price < min_price:
#                 min_price=max_price=price
#         return res
#
#
# if __name__ == '__main__':
#     prices = [7, 1,5, 3,6, 4]
#     print(Solution().maxProfit(prices))



# val = list(map(int, input("").strip().split()))
# v, a, b = val[0], val[1], val[2]
# s = input("")
# while a > 0 or b > 0:
#      if a > 0:
#          s.pop(s[0])
#          a -=1
#      if b > 0 :
#          s.pop()
#          b-=1
# print(s)


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        val = ""
        l = min(len(strs[0]),len(strs[2]),len(strs[1]))
        for i in range(l):
            if strs[0][i] == strs[1][i] and strs[0][i] == strs[2][i]:
                val = val + strs[0][i]
        print(val)


if __name__ == '__main__':
    s = Solution()
    s.longestCommonPrefix(["abc","ab","abcd"])