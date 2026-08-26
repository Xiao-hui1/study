# from collections import *
# import heapq as hp
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     d = list(map(int, input().split()))
#     d.sort(reverse=True)
#     if n < 5 or sum(d) % 5 != 0 or max(d) > sum(d) // 5 :
#         print("F")
#     else:
#         print("T")


# n = int(input())
# for _ in range(n):
#     t = int(input())
#     d = list(map(int, input().split()))
#     count = 0
#     for i in range(t):
#         if i == 1:
#             count += 1
#         else:
#             count += 2
#     if count % 2:
#         print('L')
#     else:
#         print('Q')

# n = int(input())
# d = list(map(int, input().split()))
# s = 0
# for l in range(1, n + 1):
#     for r in range(l, n + 1):
#         p = len(str(r - l + 1))
#         m = max(d[l - 1: r])
#         s += p * m % 998244353
# print(s)


# t = int(input())
# for i in range(t):
#     n = int(input())
#     if n % 2 == 0:
#         print(n)
#     else:
#         print(n + 1)


# s = "kfdhtshmrw4nxg#f44ehlbn33ccto#mwfn2waebry#3qd1ubwyhcyuavuajb#vyecsycuzsmwp31ipzah#catatja3kaqbcss2th"
# l = 0
# r = len(s)
# ans = 0
# while l < r:
#     num = 0
#     for j in range(16):
#         if  l + j >= len(s):
#             break
#         if s[l + j] in ['1', '2', '3', '4', '5', '6', '7', '8', '9','0']:
#             num += 1
#         if j >= 7 and num != 0 and num != (j + 1):
#             ans += 1
#             print(s[l: l + j + 1])
#     l += 1
# print(ans)


# n, m = map(int, input().split())
# s = list(input().strip())
# d = list(input().strip())
# d.sort()
# i = 0
# j = 0
# while i < n and j < m:
#     if s[i] <= d[j]:
#         print(s[i],end='')
#         i += 1
#     else:
#         print(d[j],end='')
#         j += 1
#
# if i == len(s):
#     print("".join(d[j:]),end='')
# else:
#     print("".join(s[i:]))


# n = int(input())
# d = [0] + list(map(int, input().split()))
# dp = [set() for i in range(n + 1)]
# ans = 0
# for i in range(n, 0, -1):
#     if i * 2 <= n:
#         dp[i] |= (dp[i * 2])
#     if i + d[i] <= n:
#         dp[i] |= dp[i + d[i]]
#     dp[i].add(d[i])
#     ans = max(len(dp[i]), ans)
# print(ans)



# import math, collections
#
# d = collections.defaultdict(int)
#
# def fun(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     g = math.gcd(abs(dy), (dx))
#     for i in range(g + 1):
#         x = x1 + i * dx // g
#         y = y1 + i * dy // g
#         d[(x, y)] += 1
#
# n = int(input())
# for i in range(n):
#     x1, y1, x2, y2 = map(int, input().split())
#     fun(x1, y1, x2, y2)
# ans = 0
# for i in d.keys():
#     if d[i] > 1:
#         ans += 1
#
# print(ans)

# import sys
# input = sys.stdin.readline
#
# def solve():
#     n, c, b = map(int, input().split())
#     s = [0] + list(map(int, input().split()))
#     a = [0] + list(map(int, input().split()))
#     dp = [0] * (n + 1)
#     ans = 0
#     dp[0] = b
#     f = 1
#     for i in range(1, n + 1):
#         sum = 9**18
#         for j in range(i, -1, -1):
#             dp[j] = min(dp[j] + s[i], c)
#             if j:
#                 dp[j] = max(min(dp[j - 1] + 2 * s[i], c), dp[j])
#             if dp[j] >= a[i]:
#                 sum = min(sum, j)
#             else:
#                 dp[j] = -float('inf')
#
#         ans = max(ans, sum)
#         if ans == 9**18:
#             print(-1)
#             return
#     print(ans)
#     return
#
# if "__main__" == __name__:
#     solve()


# import collections
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     d = []
#     for i in range(n):
#         s = input().split()
#         d.append(s)
#     d = sorted(d,key = lambda x: (x[0], x[2]))
#     mp = collections.defaultdict(list)
#     per = [[0] * 26]*100003
#     cur = 0
#     for i in range(n):
#         if cur != 0 and d[i][0] != d[i-1][0]:
#             cur += 1
#         if d[i][3] =='Rejected':
#             per[cur][ord(d[i][1] - 'A')] += 20
#         if d[i][3] == 'Accepted':
#             mp[d[i][0]] =


# import sys
# from collections import Counter
#
# MOD = 998244353
# INV2 = (MOD + 1) // 2
#
# input = sys.stdin.readline
#
#
# def solve():
#
#     T = int(input())
#
#     MAXN = 200005
#
#     pow2 = [1] * (MAXN + 5)
#     pow3 = [1] * (MAXN + 5)
#
#     for i in range(1, MAXN + 5):
#         pow2[i] = pow2[i-1] * 2 % MOD
#         pow3[i] = pow3[i-1] * 3 % MOD
#
#
#     ans = []
#
#     for _ in range(T):
#
#         n = int(input())
#
#         a = list(map(int,input().split()))
#
#         cnt = Counter(a)
#
#         res = 0
#
#         less = 0
#
#         for x,c in sorted(cnt.items()):
#
#             L = less
#
#             # 3^L(3^C-1)
#             part1 = (
#                 pow3[L] *
#                 (pow3[c]-1)
#             ) % MOD
#
#
#             # (2^C-1)(3^L-1)
#             part2 = (
#                 (pow2[c]-1) *
#                 (pow3[L]-1)
#             ) % MOD
#
#
#             coef = (part1 - part2) % MOD
#             coef = coef * INV2 % MOD
#
#
#             res = (
#                 res +
#                 x * coef
#             ) % MOD
#
#
#             less += c
#
#
#         ans.append(str(res))
#
#
#     print("\n".join(ans))
#
#
# if __name__ == "__main__":
#     solve()


import math
