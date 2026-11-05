"""
Tarjan 离线求 LCA（最近公共祖先）

适用：一棵树（或森林）上一次性给出全部询问，一次 DFS 求出所有答案。
时间复杂度约 O(n + q)，瓶颈是并查集，带路径压缩后近似线性。

和倍增、欧拉序 + 稀疏表的区别：
    倍增 / ST 是在线的，来一个问一个。
    Tarjan 是离线的，必须先拿到全部询问，再统一回答。

做法：
    1. 每个询问 (u, v) 挂到 u 和 v 两边。后访问到的那一端负责回答。
    2. 从根 DFS。进入 u 时，u 单独成一个集合，祖先记为 u。
    3. 一棵子树访问完，把该子树并到 u，并把集合代表元的祖先改成 u。
       不能按秩合并，否则代表元可能不是当前这条根到 u 的路径上的点。
    4. u 的子树都处理完后，检查挂在 u 上的询问。
       若另一端 v 已经访问过，LCA(u, v) = ancestor[find(v)]。

为什么答案是 ancestor[find(v)]，而不是 find(v) 本身：
    并查集的 parent 只负责“这堆点目前挂在谁下面”。
    ancestor 才记录“这堆点目前已知的最近公共祖先”。
    教科书写法允许合并后代表元不是树上的当前节点，所以两者要分开存。
    本实现始终把子树挂到当前节点 u 上，因此代表元恰好就是 u，
    ancestor[u] 也是 u。分开存是为了和标准 Tarjan 对应，不容易写错。

输入（1 开始编号）：
    第一行 n q
    接下来 n - 1 行，每行一条树边 u v
    接下来 q 行，每行一个询问 u v
    输出 q 行，第 i 行是第 i 个询问的 LCA
"""

import sys

sys.setrecursionlimit(1_000_000)


class TarjanLCA:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]
        self.queries = [[] for _ in range(n + 1)]
        self.parent = list(range(n + 1))
        self.ancestor = list(range(n + 1))
        self.visited = [False] * (n + 1)
        self.answer = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def add_query(self, u, v):
        idx = len(self.answer)
        self.answer.append(0)
        self.queries[u].append((v, idx))
        if u != v:
            self.queries[v].append((u, idx))
        return idx

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def _dfs(self, u, father):
        self.visited[u] = True
        self.parent[u] = u
        self.ancestor[u] = u

        for v in self.graph[u]:
            if v == father:
                continue
            self._dfs(v, u)
            # 子树处理完，整棵子树并到 u。方向必须是“子 -> 当前点”。
            self.parent[self.find(v)] = u
            self.ancestor[self.find(u)] = u

        for v, idx in self.queries[u]:
            if self.visited[v]:
                self.answer[idx] = self.ancestor[self.find(v)]

    def solve(self, root=1):
        self._dfs(root, 0)
        return self.answer

    def solve_forest(self):
        """根不连通、或有多棵树时，对每个未访问点再做一次 DFS。"""
        for u in range(1, self.n + 1):
            if not self.visited[u]:
                self._dfs(u, 0)
        return self.answer


def solve_from_input(data=None):
    if data is None:
        data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    lca = TarjanLCA(n)
    for _ in range(n - 1):
        lca.add_edge(int(next(it)), int(next(it)))
    for _ in range(q):
        lca.add_query(int(next(it)), int(next(it)))
    return lca.solve(1)


if __name__ == "__main__":
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    #         \
    #          7
    demo = TarjanLCA(7)
    for u, v in ((1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (5, 7)):
        demo.add_edge(u, v)
    queries = [(4, 5), (4, 6), (7, 5), (7, 6), (4, 4), (2, 7)]
    expected = [2, 1, 5, 1, 4, 2]
    for u, v in queries:
        demo.add_query(u, v)
    got = demo.solve(1)
    assert got == expected, (got, expected)
    for (u, v), ans in zip(queries, got):
        print(f"LCA({u}, {v}) = {ans}")
