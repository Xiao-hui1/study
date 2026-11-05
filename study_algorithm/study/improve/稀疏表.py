import math, sys

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

# f[j][i] 表示从下标 j 开始、长度为 2^i 的区间最大值（下标从 1 开始）
f = [[0] * (int(math.log2(n)) + 1) for _ in range(n + 1)]


def create():
    for i in range(1, n + 1):
        f[i][0] = a[i - 1]
    k = int(math.log2(n))
    for i in range(1, k + 1):
        for j in range(1, n - (1 << i) + 2):
            f[j][i] = max(f[j][i - 1], f[j + (1 << (i - 1))][i - 1])


def query(l, r):
    k = int(math.log2(r - l + 1))
    return max(f[l][k], f[r - (1 << k) + 1][k])


create()
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    print(query(l, r))

"""
    在线区间最值查询算法
        根据树建立一个欧拉序列：
            先对树进行dfs遍历，然后回溯，把其中的所有节点都记录下来就是欧拉序列了
            进行dfs的时候需要同时记住当前节点第一次出现的下标，以及深度
            最后u, v 的公共祖先的位置就在u, v 在欧拉序列中第一次出现的那个区域之中，深度最小的就是他们的公共祖先了
"""
"""
    离线tarjan算法
        利用并查集进行操作
        首先从根节点开始进行dfs 建立一个数组，来记录那些节点已经被访问过了，并且初始化并查集的集合号为自己本身，
        当dfs到达叶子节点的时候，进行检查当前节点是否为要查询的公共祖先的节点之一，如果不是则更新集合号为他的父节点，并且回退到父节点的位置
        如果是查询的节点，则判断一下另一个节点是否已经被访问过了，如果没有则什么也不做，继续进行访问和回退，知道两个节点都被访问了，则返回另一个节点的祖先
"""


class Unionfind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        a = self.find(u)
        b = self.find(v)
        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
        else:
            self.parent[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1


def tarjan(n, edges, queries, root=0):
    ans = [0] * len(queries)

    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    aim = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(queries):
        aim[u].append((v, idx))
        aim[v].append((u, idx))

    uf = Unionfind(n)
    visited = [False] * n

    def dfs(root, parent):
        visited[root] = True  # 标记为已经访问了
        for v in graph[root]:
            if v != parent:
                dfs(v, root)
                # 回溯时把子节点所在集合定向挂到当前节点名下，
                # 保证 find 返回的是当前递归路径上的祖先（不能用按秩合并，方向会反）
                uf.parent[uf.find(v)] = root

        # 查找相关查询
        for v, idx in aim[root]:
            if visited[v]:
                ans[idx] = uf.find(v)

    dfs(root, -1)
    return ans


if __name__ == "__main__":
    n = 7
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [4, 6]]
    queries = [[3, 6], [5, 6], [4, 3]]  # 待查询列表

    # 求解LCA
    lca_results = tarjan(n, edges, queries, root=0)

    # 输出结果（对应图解最终结果）
    for i, (u, v) in enumerate(queries):
        print(f"LCA({u}, {v}) = {lca_results[i]}")
