# from collections import defaultdict
#
#
# class Kruskal:
#     def __init__(self, n):
#         self.rank = [0] * (n + 1)
#         self.fa = range(n + 1)
#
#     def find(self, x):
#         if x != self.fa[x]:
#             x = self.find(self.fa[x])
#         return self.fa[x]
#
#     def union(self, u, v) -> bool:
#         x , y = self.find(u), self.find(v)
#         if x == y:
#             return False
#
#         if self.rank[x] > self.rank[y]:
#             self.rank[y] = x
#         elif self.rank[x] < self.rank[y]:
#             self.rank[x] = y
#         else:
#             self.rank[y] = x
#             self.rank[x] += 1
#         return True
#
# def kruskal(n, edges):
#     edges.sort()
#
#     uf = Kruskal(n)
#     m_cost = 0
#     edges_use = 0
#     for w, u, v in edges:
#         if uf.union(u, v):
#             m_cost += w
#             edges_use += 1
#
#             if edges_use == n - 1:
#                 break
#
#     return m_cost
#
# if __name__ == '__main__':
#     n, m = map(int, input().split())
#     edges = []
#     for _ in range(m):
#         w, u, v = map(int, input().split())
#         edges.append((w, u, v))
#
#     res = kruskal(n, edges)
#     print(res)
from collections import deque

# import collections
#
# def solve():
#     n = int(input())
#     d = list(map(int, input().split()))
#     mp = collections.defaultdict(int)
#     ans = 0
#     for i in range(n):
#         if d[i] % 7 == 0:
#             mp[(d[i] // 7, 7)] += 1
#         if d[i] % 3 == 0:
#             mp[(d[i] // 3, 3)] += 1
#         if d[i] % 5 == 0:
#             ans += (mp[(d[i] // 5, 7)] * mp[(d[i] // 5, 3)])
#     mp.clear()
#     for i in range(n - 1, -1, -1):
#         if d[i] % 7 == 0:
#             mp[(d[i] // 7, 7)] += 1
#         if d[i] % 3 == 0:
#             mp[(d[i] // 3, 3)] += 1
#         if d[i] % 5 == 0:
#             ans += (mp[(d[i] // 5, 7)] * mp[(d[i] // 5, 3)])
#     print(ans)
#
# if __name__ == '__main__':
#     solve()





from collections import deque
import sys
input = sys.stdin.readline

n , k = map(int, input().split())
d = list(map(int, input().split()))

def check(limit) -> bool:
    far = [0] * n
    mx = deque()
    mn = deque()

    r = 0
    for l in range(n):
        while r < n:
            # 利用单调队列计算区间最大值
            while mx and d[mx[-1]] <= d[r]:
                mx.pop()
            mx.append(r)
            #同理计算区间最小值
            while mn and d[mn[-1]] >= d[r]:
                mn.pop()
            mn.append(r)

            cur_max = d[mx[0]]
            cur_min = d[mn[0]]

            if cur_max - cur_min + (r - l + 1) <= limit:
                r += 1
            else:
                if mx and mx[-1] == r:
                    mx.pop()
                if mn and mn[-1] == r:
                    mn.pop()
                break
        far[l] = r - 1
        if mx and mx[0] == l:
            mx.popleft()
        if mn and mn[0] == l:
            mn.popleft()

    cnt = 0
    pos = 0

    #如果当前的分法不满足分成<=k, return false else true;，
    while pos < n:
        cnt += 1
        pos = far[pos] + 1
        if cnt > k:
            return False

    return True

L = 1
R = max(d) - min(d) + n
while L < R:
    mid = (L + R) // 2
    if check(mid):
        R = mid
    else:
        L = mid + 1
print(L)