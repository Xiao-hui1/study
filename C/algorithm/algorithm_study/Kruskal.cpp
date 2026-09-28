#include <bits/stdc++.h>
using namespace std;

struct Edge
{
    int from;
    int to;
    long long weight;

    bool operator<(const Edge &other) const
    {
        return weight < other.weight;
    }
};

class DisjointSet
{
public:
    explicit DisjointSet(int vertexCount) : parent(vertexCount + 1), size(vertexCount + 1, 1)
    {
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int vertex)
    {
        if (parent[vertex] != vertex)
            parent[vertex] = find(parent[vertex]);
        return parent[vertex];
    }

    bool unite(int firstVertex, int secondVertex)
    {
        int firstRoot = find(firstVertex);
        int secondRoot = find(secondVertex);
        if (firstRoot == secondRoot)
            return false;

        if (size[firstRoot] < size[secondRoot])
            swap(firstRoot, secondRoot);

        parent[secondRoot] = firstRoot;
        size[firstRoot] += size[secondRoot];
        return true;
    }

private:
    vector<int> parent;
    vector<int> size;
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int vertexCount, edgeCount;
    cin >> vertexCount >> edgeCount;

    vector<Edge> edges(edgeCount);
    for (Edge &edge : edges)
        cin >> edge.from >> edge.to >> edge.weight;

    // 按边权从小到大尝试加入；只有连接两个不同连通块时才不会形成环。
    sort(edges.begin(), edges.end());
    DisjointSet components(vertexCount);
    long long totalWeight = 0;
    int selectedEdges = 0;

    for (const Edge &edge : edges)
    {
        if (!components.unite(edge.from, edge.to))
            continue;

        totalWeight += edge.weight;
        selectedEdges++;

        // n 个顶点的生成树恰好有 n - 1 条边，可提前结束。
        if (selectedEdges == vertexCount - 1)
            break;
    }

    if (selectedEdges != vertexCount - 1)
        cout << "Impossible\n";
    else
        cout << totalWeight << '\n';

    return 0;
}