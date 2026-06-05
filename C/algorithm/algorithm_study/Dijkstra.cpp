#include <bits/stdc++.h>
using namespace std;
// using ll = long long;
typedef long long ll;
// typedef long long int;
constexpr const ll N = 1e6 + 1;

constexpr const ll inf = 4e12;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n;

    vector<vector<pair<ll, int>>> graph(n + 1);
    vector<ll> dist(n + 1, inf);
    // vector<int> p(n + 1, -1);

    cin >> q;

    // 建立无向图
    for (int i = 0; i < q; i++)
    {
        int x, y, v;
        cin >> x >> y >> v;
        graph[x].push_back({y, v});
        graph[y].push_back({x, v});
    }

    // 使用优先队列来记录,剩余的节点
    priority_queue<
        pair<ll, int>,
        vector<pair<ll, int>>,
        greater<pair<ll, int>>>
        pq;

    int s = 1; // 起点
    dist[s] = 0;
    pq.push({0, s});
    while (!pq.empty())
    {
        auto [d, u] = pq.top();
        pq.pop();
        if (d > dist[u])
            continue;
        for (auto [v, w] : graph[u])
        {
            if (dist[v] > dist[u] + w)
            {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }

    for (int i = 1; i <= n; i++)
    {
        if (dist[i] == inf)
            cout << -1 << endl;
        else
            cout << dist[i] << endl;
    }
    return 0;
}