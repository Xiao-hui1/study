"""
    最小生成树算法：
        Prim算法：（O(n^2)）
            思想：先选择任意一个节点，查找和当前这个节点相邻且位权最小的节点，把这个节点链接上来，并同时记录和新来节点相邻的节点的位权，
            用两个数组记录，一个数组记录那些节点已经连接了，和那个节点连接的，另一个数组记录，当前节点和已经建立了连接的节点中的那个节点最近，
            并且记录他的权值

"""
import heapq, sys, math, random
input = sys.stdin.readline

class Prim:
    def __init__(self, n):
        self.n = n

    def solve(self):
        data = [[] for _ in range(self.n + 1)]
        sign = [0] * (self.n + 1)
        for _ in range(self.n):
            x, y, val = map(int, input().split())
            data[x].append((y, val))
            data[y].append((x, val))

        lowcost = [float('inf')] * (self.n + 1)  # 将初始值设为无穷大
        closet = [0] * (self.n + 1)

        # 从顶点 1 开始构建MST
        sign[1] = 1
        for y, val in data[1]:
            lowcost[y] = val
            closet[y] = 1

        total_cost = 0  # 记录最小生成树的总权重

        # 还需要加入 n-1 个顶点
        for _ in range(self.n - 1):
            # 寻找未加入集合中距离最近的点 (贪心)
            min_cost = float('inf')
            v = -1
            for j in range(1, self.n + 1):
                if sign[j] == 0 and lowcost[j] < min_cost:
                    min_cost = lowcost[j]
                    v = j

            # 如果没找到，说明图不连通 (这里简单处理，实际可能需要报错)
            if v == -1:
                break

            # 将点 v 加入集合
            sign[v] = 1
            total_cost += min_cost

            # 更新与 v 相邻的点的最短距离
            for y, val in data[v]:
                if sign[y] == 0 and val < lowcost[y]:
                    lowcost[y] = val
                    closet[y] = v

        print(total_cost)



"""
    Kruskal算法
"""

class UnionFind:
    """并查集类，用于高效管理集合的合并与查询"""

    def __init__(self, n):
        self.parent = list(range(n))  # 每个元素初始时父节点是自己
        self.rank = [0] * n  # 用于按秩合并的数组，记录树的高度

    def find(self, x):
        """查找 x 的根节点（代表元），并进行路径压缩"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """合并 x 和 y 所在的集合"""
        root_x = self.find(x)
        root_y = self.find(y)

        # 如果已经在同一集合，无需合并
        if root_x == root_y:
            return False

        # 按秩合并：将低秩树挂到高秩树下
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # 秩相等时，任意挂靠，并将根的秩加1
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True


def kruskal(n, edges):
    """
    Kruskal 算法求最小生成树
    :param n: 顶点数量 (顶点编号通常为 0 到 n-1 或 1 到 n)
    :param edges: 边的列表，每个元素为 (权重, 顶点u, 顶点v)
    :return: 最小生成树的总权重
    """
    # 1. 将边按权重从小到大排序
    edges.sort()

    # 2. 初始化并查集
    uf = UnionFind(n + 1)  # 这里多开一个空间，为了兼容顶点编号从1开始的情况
    mst_cost = 0
    edges_used = 0

    # 3. 遍历所有边
    for weight, u, v in edges:
        # 4. 检查加入这条边是否会形成环
        if uf.union(u, v):
            # 如果成功合并，说明不形成环，将此边加入生成树
            mst_cost += weight
            edges_used += 1

            # 5. 如果已经选了 n-1 条边，生成树完成
            if edges_used == n - 1:
                break

    # 如果无法构成生成树（图不连通），edges_used 会 < n-1
    # 根据题目要求，这里可以返回 -1 或抛出异常
    return mst_cost


if __name__ == "__main__":
    # 输入顶点数 n 和边数 m
    n, m = map(int, input().split())
    edges = []

    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))  # 将权重放在第一位，方便排序

    result = kruskal(n, edges)
    print(result)