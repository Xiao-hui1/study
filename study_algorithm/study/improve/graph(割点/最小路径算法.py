"""
        Dijkstra算法：
            1. 建立一个dist[]数组，p[]数组，graph[][]数组，dist中存放 第i 个节点到源节点得最短路径，
            p[]数组中存放第i个节点得前驱节点，graph数组存放节点得权值
            2. 初始化数组，把源节点到相邻的节点，的距离存放在dist数组中，在p[]数组中存放源节点。
            3. 找，在dist数组中找到权值最小且没有被访问的节点，如果没有了则算法结束
            4. 判，假设当前新加入的节点为t，如果t相邻的节点j，dist[j] > dist[t] + graph[t][j]，更新最短路径和p[]数组的前驱。

"""
import sys, math, random, collections


# class Dijkstra:
#     def solve(self):
#         n = int(input())
#         g = [[] for _ in range(n + 1)]
#         for _ in range(n):
#             v, x, y = map(int, input().split())
#             g[x].append((y, v))
#             g[y].append((x, v))
#
#         dist = [math.inf] * (n + 1)
#         p = [0] * (n + 1)
#         flag = [False] * (n + 1)
#
#         # 初始化起点
#         flag[1] = True
#         for x, y in g[1]:
#             dist[x] = y
#             p[x] = 1
#
#         # 主循环：处理剩下的 n-1 个节点
#         for i in range(2, n + 1):
#             min_val = math.inf
#             k = 0
#
#             # 1. 找到距离最小的未访问节点
#             for j in range(1, n + 1):
#                 if not flag[j] and dist[j] < min_val:
#                     min_val = dist[j]
#                     k = j
#
#             # 2. 标记该节点为已访问
#             flag[k] = True
#
#             # 3. 松弛操作：用节点 k 更新其所有邻居的距离
#             for x, y in g[k]:
#                 if dist[k] + y < dist[x]:
#                     dist[x] = dist[k] + y
#                     p[x] = k
#
#         # 通常这里会输出结果，例如输出节点 n 的最短距离
#         # 如果题目要求输出路径，可以利用 p 数组回溯
#         if dist[n] == math.inf:
#             print(-1)  # 无法到达
#         else:
#             print(dist[n])
#
#
#
# def solve():
#     import heapq
#
#     n, m = map(int, input().split())
#
#     g = [[] for _ in range(n + 1)]
#     for _ in range(m):
#         u, v, w = map(int, input().split())
#         g[u].append((v, w))
#         g[v].append((u, w))
#
#     dist = [float('inf')] * (n + 1)
#     dist[1] = 0
#
#     pq = [(0, 1)]
#
#     while pq:
#         d, u = heapq.heappop(pq)
#
#         if d > dist[u]:
#             continue
#
#         for v, w in g[u]:
#             if dist[v] > d + w:
#                 dist[v] = d + w
#                 heapq.heappush(pq, (dist[v], v))
#
#     print(-1 if dist[n] == float('inf') else dist[n])
#
#
# if __name__ == '__main__':
#     solve()

import sys, collections
import heapq as hp


def Dijkstra():
    n, m = map(int, input().split())
    cost = 0
    dist = [float("inf")] * (n + 1)
    d = []
    g = [[]  for _ in range(n + 1)]
    for i in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    dist[1] = 0
    hp.heappush(d, (0, 1))
    while d:
        c, v = hp.heappop(d)
        if dist[v] < c:
            continue

        for (u, w) in g[v]:
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                hp.heappush(d, (dist[v], u))

    for i in range(1, n+1):
        if dist[i] == float("inf"):
            print(-1)
        else:
            print(dist[i])