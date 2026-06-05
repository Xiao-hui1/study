# data = ['leetcode','word','weap','foundation','federal']
# val = sorted(data, key=len)
# print(''.join(val))
# val = sorted(data, key=len, reverse=True)
# hash = [[] for _ in range(len(val[0])) ]
# s= 'bb'
# print(s[0:1])
# print(hash)
# val.sort()
# print(val)

#此算法为失败算法:  尝试对象为leetcode .139题
# class Solution:
#     def match(self,text, sub):
#         for i in range(len(text)):
#             if text[i] != sub[i]:
#                 return 0
#         return 1
#
#     def values(self,st) -> int:
#         num = 0
#         st = str(st)
#         for i in st:
#             num += ord(i)
#         return num
#
#     def wordBreak(self, s: str, wordDict: list[str]) -> bool:
#         val = sorted(wordDict, key = len)
#
#         hash = [[] for _ in range(len(val[-1]))]
#
#         word_len = list(set(len(i) for i in val))
#         word_len.sort()
#         for i in val:
#             num = self.values(i)
#             hash[len(i)-1].append(num)
#         length = 0
#         while length < len(s):
#             flag = False
#             for i in word_len:
#                 if length + i <= len(s) and self.values(s[length: length + i]) in hash[i-1]:
#                     for v in list(filter(lambda x: len(x) == i, val)):
#                         if self.match(s[length : length + i], v):
#                             print(v)
#                             flag = True
#                             length += i
#             if not flag:
#                 return False
#
#         return True
#
# if __name__ == '__main__':
#     s = Solution()
#     print(s.wordBreak('aaaaaaa', ["aaa", "aaaa"]))

class Solution:
    def longestPalindrome(self, s: str) -> int:
        data = set(s)
        val = {}
        for i in data:
            val[i] = 0
        for i in s:
            val[i] += 1
        res = 0
        for i in val.values():
            if not i%2:
                res += i
        return res + 1


if __name__ == '__main__':
    # s = Solution()
    # print(s.longestPalindrome("abccccdd"))

    # num = int(input())
    # data = []
    # flag = False
    # own = []
    #
    # for i in range(num):
    #     if not flag:
    #         data.append(list(map(int, input().split())))
    #         own.extend(data[-1])
    #         flag = True
    #     else:
    #         data.append(list(map(int, input().split())))
    # res = sorted(data, key=lambda x: (x[0],-x[0]), reverse=True)
    # idx = res.index(own) + 1
    # print(idx)
    # if idx <= int(num * 0.1):
    #     print("gold")
    # elif int(num * 0.1) < idx <= int(num * 0.3):
    #     print("silver")
    # elif int(num * 0.3) < idx <= int(num * 0.6):
    #     print("bronze")
    # else:
    #     print("iron")

    # num = int(input())
    # val = input()
    # stack = []
    # ma = 0
    # for i in val:
    #     if i == '(' and len(stack) == 0:
    #         stack.append('(')
    #     elif i == '(' and len(stack) != 0:
    #         stack = ['(']
    #         print(stack)
    #     if i == '#' and len(stack) != 0:
    #         stack.append('#')
    #         print(stack)
    #     if i == ')' and len(stack) != 0:
    #         if ma < len(stack) + 1:
    #             ma = len(stack) + 1
    #         stack = []
    # print(ma)

    num = int(input())
    data = []
    res = []
    for i in range(num):
        li = input().split()
        data.append(li)
    val = []
    for i in data:
        if i not in val:
            val.append(i)
    idx = 0
    val = sorted(val, key = lambda x: x[0])
    while idx < len(val) - 1:
        if val[idx][0] == val[idx + 1][0]:
            x = data.index(val[idx])
            y = data.index(val[idx + 1])
            res.append([x + 1,y + 1])
            idx += 2
        else:
            idx += 1
    if res:
        for i in res:
            print(f"{i[0]} {i[1]}")
    else:
        print(0)

