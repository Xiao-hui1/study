"""
拓扑排序模板
1. Kahn 算法（BFS，入度法）—— 最常用
2. 字典序最小的拓扑序 —— 用堆替代队列
3. 判断是否有环
4. DFS 版本
"""

from collections import deque
import heapq
import sys

sys.setrecursionlimit(10**6)


def topo_sort(n, edges):
    """Kahn 算法。n 为点数（编号 0~n-1），edges 为 (u, v) 表示 u -> v。
    返回拓扑序；若有环则返回 None。"""
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1

    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return order if len(order) == n else None  # 长度不足 n 说明有环


def topo_sort_lex_smallest(n, edges):
    """字典序最小的拓扑序：把队列换成小根堆。"""
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1

    h = [i for i in range(n) if indeg[i] == 0]
    heapq.heapify(h)
    order = []
    while h:
        u = heapq.heappop(h)
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(h, v)

    return order if len(order) == n else None


def topo_sort_dfs(n, edges):
    """DFS 版本：逆后序即拓扑序。返回 None 表示有环。"""
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)

    state = [0] * n  # 0=未访问, 1=访问中, 2=已完成
    order = []
    has_cycle = False

    def dfs(u):
        nonlocal has_cycle
        state[u] = 1
        for v in g[u]:
            if state[v] == 1:
                has_cycle = True
                return
            if state[v] == 0:
                dfs(v)
        state[u] = 2
        order.append(u)

    for i in range(n):
        if state[i] == 0:
            dfs(i)

    if has_cycle:
        return None
    return order[::-1]


if __name__ == "__main__":
    # 示例：6 个点，边 0->1, 0->2, 1->3, 2->3, 3->4, 4->5
    n = 6
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5)]
    print(topo_sort(n, edges))  # [0, 1, 2, 3, 4, 5] 或其他合法序
    print(topo_sort_lex_smallest(n, edges))  # [0, 1, 2, 3, 4, 5]
    print(topo_sort_dfs(n, edges))  # [0, 2, 1, 3, 4, 5] 或其他合法序
