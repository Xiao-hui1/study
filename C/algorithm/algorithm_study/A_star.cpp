#include <bits/stdc++.h>
using ll = long long;
using namespace std;
const ll N = 100005;
/* describe:
    起点入队

    while 队列非空:

        取 f 最小点 u

        如果 u 是终点:
            return

        枚举邻居 v

            if g[v] 可以更新:

                g[v]=g[u]+w

                f[v]=g[v]+h[v]

                入队

*/

struct node
{
    int id;
    ll f, g;
    bool operator<(const node &other) const
    {
        return f > other.f; // 小根堆
    }
};

vector<pair<int, int>> g[N];
ll dist[N];

ll h(int u)
{
    return 0;
}

void Astar(int s, int t, int n)
{
    memset(dist, 0x3f, sizeof(dist));
    priority_queue<node> q;
    dist[s] = 0;
    q.push({s, h(s), 0});
    while (!q.empty())
    {
        auto cur = q.top();
        q.pop();

        int u = cur.id;

        if (u == t)
        {
            cout << dist[t] << endl;
            return;
        }

        if (cur.g > dist[u])
            continue;

        for (auto [v, w] : g[u])
        {
            if (dist[v] > dist[u] + w)
            {
                dist[v] = dist[u] + w;
                q.push({v, dist[v] + h(v), dist[v]});
            }
        }
    }
}

int main()
{
    return 0;
}