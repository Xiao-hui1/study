#include <bits/stdc++.h>
using namespace std;

struct Edge
{
    int to;
    long long weight;
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int vertexCount, edgeCount;
    cin >> vertexCount >> edgeCount;

    vector<vector<Edge>> graph(vertexCount + 1);
    for (int edgeIndex = 0; edgeIndex < edgeCount; edgeIndex++)
    {
        int from, to;
        long long weight;
        cin >> from >> to >> weight;
        graph[from].push_back({to, weight});
        graph[to].push_back({from, weight});
    }

    // 堆中保存“将某个未选顶点接入当前生成树”的最小候选边。
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> candidates;
    vector<bool> inTree(vertexCount + 1, false);
    candidates.push({0, 1});

    long long totalWeight = 0;
    int selectedVertices = 0;

    while (!candidates.empty())
    {
        auto [weight, vertex] = candidates.top();
        candidates.pop();

        // 同一顶点可能被多条候选边加入，跳过过期候选。
        if (inTree[vertex])
            continue;

        inTree[vertex] = true;
        totalWeight += weight;
        selectedVertices++;

        for (const Edge &edge : graph[vertex])
        {
            if (!inTree[edge.to])
                candidates.push({edge.weight, edge.to});
        }
    }

    // 只有全部顶点被加入，才存在覆盖所有顶点的最小生成树。
    if (selectedVertices != vertexCount)
        cout << "Impossible\n";
    else
        cout << totalWeight << '\n';

    return 0;
}