# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     sta = []
#     twist = []
#     tr = [[0] * (m + 1) for i in range(n + 1)] #当前反向，我用1 来表示向右，2表示向下
#     for _ in range(n):
#         sta.append(list(map(int, input().split())))
#     for _ in range(n):
#         twist.append(list(map(int, input().split())))
#     dp = [[0] * (m+1) for _ in range(n+1)]
#     for i in range(1, n+1):
#         for j in range(1, m+1):
#             if i == 1 and j == 1:
#                 dp[i][j] = sta[i-1][j-1]
#             else:
#                 if tr[i-1][j] == 1:
#                     dp[i][j] = min(dp[i-1][j] + twist[i-1][j] + sta[i - 1][j-1], dp[i-1][j-1] + sta[i-1][j-1])
from ast import iter_child_nodes

# t = int(input())
# import collections
# for _ in range(t):
#     n = int(input())
#     ans = collections.defaultdict(int)
#     for i in range(n):
#         a, b ,c = map(int, input().split())
#         if (c - b) % a == 0:
#             x = (c - b) // a
#             ans[x] += 1
#         if (c - a) % b == 0:
#             x = (c - a) // b
#             ans[x] += 1
#         if (b - a) % c == 0:
#             x = (b - a) // c
#             ans[x] += 1
#         if (b - c) % a == 0:
#             x = (b - c) // a
#             ans[x] += 1
#         if (a - c) % b:
#             x = (a - c) // b
#             ans[x] += 1
#         if(a - b) % c == 0:
#             x = (a - b) // c
#             ans[x] += 1
#     res = max(ans.values())
#     for x in ans.keys():
#         if ans[x] == res and x >= 0:
#             print(x)
#             break

# n , m = map(int, input().split())
# res = [[0,0] for _ in range(m)]
# data = []
# for i in range(n):
#     s = input().strip()
#     data.append(s)
#     for j in range(m):
#         if s[j] == '1':
#             res[j][1] += 1
#         else:
#             res[j][0] += 1
# score = [0] * n
# ans = [0] * m
#
# for i in range(m):
#     if not res[i][1] or not res[i][0]:
#         ans[i] = 2
#     elif res[i][1] > res[i][0]:
#         ans[i] = 0
#     else:
#         ans[i] = 1
# for i in range(n):
#     for j in range(m):
#         if ans[j] == int(data[i][j]) or ans[j] == 2:
#             score[i] += 1
# m = max(score)
# for i in range(n):
#     if score[i] == m:
#         print(i + 1,end = ' ')



# n, q = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# mi = [0] * n
# cur = []
# for i in range(n):
#     if a[i] < b[i]:
#         mi[i] = a[i]
#         cur.append('A')
#     else:
#         mi[i] = b[i]
#         cur.append('B')
# min_sum = sum(mi)
#
# for _ in range(q):
#     d = input().split()
#     c = d[0]
#     x = int(d[1])
#     v = int(d[2])
#     res = 0
#     if c == 'A':
#         pre_min = min(a[x - 1], b[x-1])
#         cur_min = min(v, b[x-1])
#         if cur_min != pre_min:
#             min_sum -= pre_min
#             min_sum += cur_min
#         a[x - 1] = v
#     else:
#         pre_min = min(a[x - 1], b[x - 1])
#         cur_min = min(v, a[x-1])
#         if cur_min != pre_min:
#             min_sum -= pre_min
#             min_sum += cur_min
#         b[x - 1] = v
#     print(min_sum)


# from collections import deque
# import sys,math
#
# input = sys.stdin.readline
#
# h, w = map(int, input().split())
# g = [input().strip() for _ in range(h)]
#
# sx = sy = gx = gy = 0
# for i in range(h):
#     for j in range(w):
#         if g[i][j] == 'S': sx, sy = i, j
#         if g[i][j] == 'G': gx, gy = i, j
#
# d0 = [[math.inf] * w for _ in range(h)]
# d1 = [[math.inf] * w for _ in range(h)]
# d0[sx][sy] = 0
# q = deque([(sx, sy, 0)])
# dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# f = 0
# while q:
#     x, y, s = q.popleft()
#     if x == gx and y == gy:
#         print(min(d0[x][y], d1[x][y]))
#         f = 1
#         break
#     for dx, dy in dir:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < h and 0 <= ny < w and g[nx][ny] != '#':
#             c, ns = g[nx][ny], s
#             ok = 0
#             if c in 'SG.':
#                 ok = 1
#             elif c == 'o':
#                 ok = s == 0
#             elif c == 'x':
#                 ok = s == 1
#             elif c == '?':
#                 ok = 1; ns ^= 1
#
#             cur = d0[x][y] if s == 0 else d1[x][y]
#             nxt = d0[nx][ny] if ns == 0 else d1[nx][ny]
#             if ok and cur + 1 < nxt:
#                 if ns == 0:
#                     d0[nx][ny] = cur + 1
#                 else:
#                     d1[nx][ny] = cur + 1
#                 q.append((nx, ny, ns))
# if not f:
#     print(-1)

from functools import lru_cache
lru_cache(maxsize=None)
print(2026*(2**2025) % 998244353)