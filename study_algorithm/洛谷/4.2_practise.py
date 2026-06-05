# # x, c = map(int, input().split())
# # print(1000 * int(x / (1000 + c)))
#
#
# # ------------------------------------
# # n = int(input())
# # d = list(map(int, input().split()))
# # start = 0
# # end = n - 1
# # while 1:
# #     if d[start] or start == n - 1:
# #         break
# #     start += 1
# # while 1:
# #     if d[end] or end == 0:
# #         break
# #     end -= 1
# # if end - start > 0:
# #     print(end - start)
# # else:
# #     print(0)
#
#
# # -----------------------------------------
# # import sys
# # input = sys.stdin.readline
# #
# # n, p = map(int, input().split())
# # a = [0] + list(map(int, input().split()))
# #
# # l = 0
# # r = n + 1
# #
# # while l + 1 <= n and a[l + 1] == 1:
# #     l += 1
# #
# # while r - 1 >= 1 and a[r - 1] == 1:
# #     r -= 1
# #
# # ans = 0
# #
# # for i in range(l + 1, p + 1):
# #     if a[i] == 1:
# #         ans += 2
# #     else:
# #         ans += 1
# #
# # for i in range(p + 1, r):
# #     if a[i] == 1:
# #         ans += 2
# #     else:
# #         ans += 1
# #
# # print(ans)





# # --------------------------------------------------
# import heapq as hp
#
# n, k = map(int, input().split())
#
# q = []
# people = 0
# t = 0
#
# for _ in range(n):
#     a, b, c = map(int, input().split())
#
#     if t < a:
#         t = a
#
#     while q and people + c > k:
#         end_time, p_count = hp.heappop(q)
#         people -= p_count
#         if end_time > t:
#             t = end_time
#
#     hp.heappush(q, (t + b, c))
#     people += c
#
#     print(t)

import sys

# 为了处理大数据输入，建议增加递归深度并使用更快的输入方式
sys.setrecursionlimit(2000)
input = sys.stdin.readline

# 读取 n 和 q
n, q = map(int, input().split())

# 初始化前缀和数组，长度为 n+1，索引 0 为 0
# a: 原始数组
# sum1: 存储 a[i] 的前缀和
# sum2: 存储 a[i] * i 的前缀和
# sum3: 存储 a[i] * i * i 的前缀和
a = [0] * (n + 1)
sum1 = [0] * (n + 1)
sum2 = [0] * (n + 1)
sum3 = [0] * (n + 1)

# 预处理阶段
for i in range(1, n + 1):
    val = int(input())  # 读取 a[i]
    a[i] = val
    sum1[i] = sum1[i - 1] + val
    sum2[i] = sum2[i - 1] + val * i
    sum3[i] = sum3[i - 1] + val * i * i

# 处理查询
for _ in range(q):
    l, r = map(int, input().split())

    # 计算区间 [l, r] 内的三个前缀和差值
    s = sum1[r] - sum1[l - 1]
    s1 = sum2[r] - sum2[l - 1]
    s2 = sum3[r] - sum3[l - 1]

    # 核心公式计算
    # 注意：Python 的整数除法 // 和 C++ 的 / (对于整数) 行为一致，但这里全是乘法减法，直接用 -
    res = (l + r) * s1 - (l - 1) * (r + 1) * s - s2

    print(res)