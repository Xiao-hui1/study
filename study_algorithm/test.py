from collections import defaultdict


class Kruskal:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.fa = range(n + 1)

    def find(self, x):
        if x != self.fa[x]:
            x = self.find(self.fa[x])
        return self.fa[x]

    def union(self, u, v) -> bool:
        x , y = self.find(u), self.find(v)
        if x == y:
            return False

        if self.rank[x] > self.rank[y]:
            self.rank[y] = x
        elif self.rank[x] < self.rank[y]:
            self.rank[x] = y
        else:
            self.rank[y] = x
            self.rank[x] += 1
        return True

def kruskal(n, edges):
    edges.sort()

    uf = Kruskal(n)
    m_cost = 0
    edges_use = 0
    for w, u, v in edges:
        if uf.union(u, v):
            m_cost += w
            edges_use += 1

            if edges_use == n - 1:
                break

    return m_cost

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        w, u, v = map(int, input().split())
        edges.append((w, u, v))

    res = kruskal(n, edges)
    print(res)