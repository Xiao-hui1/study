#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
constexpr const ll N = 200005;
vector<int> graph[N];
vector<pair<int, int>> q[N];
int ans[N], parent[N], ancestor[N];
bool vis[N];

// 并查集
int find(int u)
{
    if (parent[u] != u)
        parent[u] = find(parent[u]);
    return parent[u];
}

// 正片 tarjan离线
void tarjan(int u)
{
    parent[u] = u;
    ancestor[u] = u;
    vis[u] = true;

    for (int v : graph[u])
    {
        if (!vis[v])
        {
            tarjan(v);
            parent[find(v)] = u;
            // 更新祖先
            ancestor[find(u)] = u;
        }
    }

    for (auto [v, id] : q[u])
    {
        if (vis[v])
        {
            ans[id] = ancestor[find(v)];
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, qu;
    cin >> n >> qu;

    for (int i = 1; i < n; i++)
    {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i = 0; i < qu; i++)
    {
        int u, v;
        cin >> u >> v;
        q[u].push_back({v, i});
        q[v].push_back({u, i});
    }

    tarjan(1);

    for (int i = 0; i < qu; i++)
    {
        cout << ans[i] << endl;
    }
    return 0;
}