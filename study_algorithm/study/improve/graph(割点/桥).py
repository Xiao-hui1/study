import sys
from collections import defaultdict


def find_cut_points_and_bridges(n, edges):
    """
    寻找无向连通图的割点和桥

    参数:
    n: 节点数量 (节点编号从 1 到 n)
    edges: 边的列表，例如 [(1,2), (2,3), (1,3)]

    返回:
    cut_points: 割点列表
    bridges: 桥的列表 (元组形式)
    """

    # 构建邻接表
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Tarjan 算法所需变量
    discovery = {}  # 发现时间戳
    low = {}  # 能够回溯到的最早的时间戳
    parent = {}  # 父节点
    visited = set()
    time = [0]  # 使用列表包装以便在递归中修改
    cut_points = set()
    bridges = []


    def dfs(u):
        # 标记当前节点已访问，并记录发现时间和 low 值
        visited.add(u)
        discovery[u] = time[0]
        low[u] = time[0]
        time[0] += 1

        children = 0  # 记录 DFS 树中该节点的子节点数量

        for v in graph[u]:
            # 如果 v 未被访问过，v 是 u 的子节点
            if v not in visited:
                parent[v] = u
                children += 1
                dfs(v)

                # 递归返回后，更新 u 的 low 值
                low[u] = min(low[u], low[v])

                # 判断是否为桥
                if low[v] > discovery[u]:
                    bridges.append((min(u, v), max(u, v)))  # 排序以避免重复

                # 判断是否为割点 (非根节点情况)
                # 如果 u 不是根节点，且子节点 v 无法回溯到 u 的祖先，则 u 是割点
                if u != 1 and low[v] >= discovery[u]:
                    cut_points.add(u)

            # 如果 v 已被访问过，且 v 不是 u 的父节点，说明是回边
            elif v != parent.get(u, None):
                low[u] = min(low[u], discovery[v])

        # 特判：根节点 (起点) 是否为割点
        # 如果根节点在 DFS 树中有超过 1 个子节点，则它是割点
        if u == 1 and children > 1:
            cut_points.add(u)

    # 假设图是连通的，从节点 1 开始 DFS
    # 如果图不连通，需要遍历所有未访问节点
    dfs(1)

    return sorted(list(cut_points)), sorted(bridges)


# ==========================================
# 🧪 示例与测试
# ==========================================

if __name__ == "__main__":
    # 示例输入
    # 一个简单的环：1-2-3-1，此时没有割点，也没有桥
    # 如果加上边 3-4，则 3 是割点，边 (3,4) 是桥

    n = 4
    edges = [(1, 2), (2, 3), (3, 1), (3, 4)]

    cuts, bridges = find_cut_points_and_bridges(n, edges)

    print("割点:", cuts)
    print("桥:", bridges)


"""
        有向图的强连通分量
    
"""


from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def tarjan_scc(self):
        # dfn: 发现时间, low: 能回溯到的最早祖先
        dfn = [-1] * self.V
        low = [-1] * self.V
        # 栈用于存储当前路径的节点
        stack = []
        # 标记节点是否在栈中
        in_stack = [False] * self.V
        # 存储结果
        scc_list = []

        def dfs(u):
            # 初始化时间戳
            dfn[u] = self.Time
            low[u] = self.Time
            self.Time += 1
            stack.append(u)
            in_stack[u] = True

            # 遍历邻居
            for v in self.graph[u]:
                if dfn[v] == -1: # 如果未访问
                    dfs(v)
                    # 回溯时更新 u 的 low 值
                    low[u] = min(low[u], low[v])
                elif in_stack[v]: # 如果已访问且在栈中 (后向边/横叉边)
                    low[u] = min(low[u], dfn[v])

            # 如果 u 是强连通分量的根
            if low[u] == dfn[u]:
                scc = []
                # 将栈中从 u 开始的所有节点弹出，构成一个 SCC
                while True:
                    w = stack.pop()
                    in_stack[w] = False
                    scc.append(w)
                    if w == u:
                        break
                scc_list.append(scc)

        # 对每个未访问的节点进行 DFS
        for i in range(self.V):
            if dfn[i] == -1:
                dfs(i)

        return scc_list

# ==========================================
# 🧪 测试示例
# ==========================================

if __name__ == "__main__":
    # 创建一个包含 5 个节点的图 (0 到 4)
    # 构造一个包含多个环的图
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0) # 环 0-1-2
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 3) # 环 3-4

    print("强连通分量：")
    result = g.tarjan_scc()
    for i, scc in enumerate(result):
        print(f"分量 {i+1}: {scc}")