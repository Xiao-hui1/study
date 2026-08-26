# count = 0
# def fun1(a):
#     s = 0
#     while a:
#         s += a % 2
#         a //= 2
#     return s
# print(63)
from sys import meta_path

# mod = 10 ** 9 + 7
# ans = (pow(9, 10000) - 2 * pow(8, 10000) + pow(7, 10000)) % mod
# print(157509472)
# print(465864330)


# n, m = map(int, input().split())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
# ans = 0
#
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         mn1 = min(n - i, m - j)
#         mn2 = min(n - i, j + 1)
#
#         for k in range(1, mn1 + 1):
#             if i + k <= n and j + k <= m:
#                 ans += int(a[i][j] == a[i + k][j + k])
#
#         for k in range(1, mn2 + 1):
#             if i + k <= n and j - k >= 0:
#                 ans += int(a[i][j] == a[i + k][j - k])
#
# print(ans * 2)


# from datetime import *
#
# n = int(input())
# for i in range(n):
#     ymd, hms, x = input().split()
#     year, month, day = ymd.split("-")
#     hour, minute, second = hms.split(":")
#     current = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
#     x = int(x)
#     periods = int((current - datetime(1970, 1, 1, 0, 0, 0)).total_seconds()) // 60 // x
#     ans = datetime(1970, 1, 1, 0, 0, 0)
#     ans += timedelta(minutes = periods * x)
#     print(ans)

# i = 1
# boss = 2025
# while 0 < boss:
#     boss -= 5
#     if i % 2 == 0:
#         boss -= 2
#     else:
#         boss -= 15
#     if i % 3 == 1:
#         boss -= 2
#     elif i  % 3 == 2:
#         boss -= 10
#     elif i % 3 == 0:
#         boss -= 7
#     i += 1

# w, h, v = map(int, input().split())
# for i in range(h):
#     print('Q'* w)
# for i in range(w):
#     print('Q'*(v + w))

# possibility = ['lqb','lbq', 'qlb', 'qbl', 'blq', 'bql']
# ha = ord('l') + ord('q') + ord('b')
# st = input().strip()
# h = []
# size = len(st)
# count = 0
# for i in range(size):
#     h.append(ord(st[i]))
# i = 2
# while i < size:
#     if h[i-1] + h[i] + h[i-2] == ha:
#         if st[i - 2: i + 1] in possibility:
#             count += 1
#             i += 2
#     i += 1
# print(count)

# 园艺
# n = int(input())
# d = list(map(int, input().split()))
# res = [-1] * n
# stack = []
# for i in range(n):
#     while stack and d[stack[-1]] > d[i]:
#         stack.pop()
#     if stack:
#         res[i] = stack[-1]
#     stack.append(i)
# ans = [0] * n
#
# for i in range(n):
#     if res[i] != -1:
#         ans[i] = i - res[i]
# import collections
# result = collections.Counter(ans)
# m = -1
# pre = -1
# pos = -1
# so = sorted(result, key = lambda x: result[x])
# for i in result.keys():
#     count = 0
#     if m >= result[i]:
#         break
#     for j in range(n):
#         if ans[j] == i and pre == -1 or pre < d[j]:
#             pre = d[j]
#             count += 1
#         else:
#             break
#     if count > m:
#         m = count
#         pos = i
#
# for i in range(n):
#     if ans[i] == pos:
#         if i - pos == 0:
#             m += 1
#         break
# print(m)

n = int(input())
h = list(map(int, input().split()))

max_trees = 1

for gap in range(1, n):
    dp = [1] * n
    for i in range(gap, n):
        if h[i - gap] < h[i]:
            dp[i] = dp[i - gap] + 1
    max_trees = max(max_trees, max(dp))

print(max_trees)