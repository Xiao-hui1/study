#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int n;

// 二分图的染色判定

bool isbipartite(int n, vector<vector<int>> &graph)
{
    vector<int> color(n, -1);
    for (int start = 0; start < n; start++)
    {
        if (color[start] != -1)
            continue;
        queue<int> q;
        q.push(start);
        color[start] = 0;
        while (!q.empty())
        {
            int u = q.front();
            q.pop();
            for (int v : graph[u])
            {
                if (color[v] == -1)
                {
                    color[v] = color[u] ^ 1; // 交叉染色
                    q.push(v);
                }
                else if (color[v] == color[u])
                {
                    return false;
                }
            }
        }
    }
    return true;
}

// 匈牙利算法 求最大匹配
const ll MAXN = 10005;
class solve
{
public:
    int n;
    vector<int> g[MAXN];
    int matchR[MAXN];
    bool vis[MAXN];
    solve() {};
    ~solve() {};
    bool dfs(int u)
    {
        for (int v : g[u])
        {
            if (!vis[v])
            {
                vis[v] = true;
                if (matchR[v] = -1 || dfs(matchR[v]))
                {
                    matchR[v] = u;
                    return true;
                }
            }
        }
        return false;
    };
    int hungarian(int n, int m)
    {
        memset(matchR, -1, sizeof(matchR));
        int res = 0;

        for (int u = 0; u < n; u++)
        {
            memset(vis, false, sizeof(vis));
            if (dfs(u))
                res++;
        }
        return res;
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    return 0;
}