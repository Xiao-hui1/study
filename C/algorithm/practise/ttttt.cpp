// // // // #include <bits/stdc++.h>

// // // // using namespace std;
// // // // using ll = long long;

// // // // int main()
// // // // {
// // // //     int t, n, m;
// // // //     cin >> t;
// // // //     for (int i = 0; i < t; i++)
// // // //     {
// // // //         cin >> n >> m;
// // // //         vector<int> a(n), b(n), c(n);
// // // //         vector<ll> ans;
// // // //         for (int j = 0; j < n; j++)
// // // //         {
// // // //             cin >> a[j];
// // // //         }
// // // //         for (int j = 0; j < n; j++)
// // // //         {
// // // //             cin >> b[j];
// // // //         }
// // // //         for (int j = 0; j < n; j++)
// // // //         {
// // // //             cin >> c[j];
// // // //         }
// // // //         sort(a.begin(), a.end());
// // // //         sort(b.begin(), b.end());
// // // //         sort(c.begin(), c.end());
// // // //         priority_queue<tuple<ll, int, int, int>, vector<tuple<ll, int, int, int>>, greater<>> d;
// // // //         d.push({((ll)a[0] * b[0] * c[0]), 0, 0, 0});
// // // //         set<tuple<int, int, int>> vis;
// // // //         vis.insert({0, 0, 0});
// // // //         while (d.size())
// // // //         {
// // // //             auto [w, x, y, z] = d.top();
// // // //             ans.push_back(w);
// // // //             d.pop();
// // // //             if (x + 1 < n && (vis.find({x + 1, y, z}) == vis.end()))
// // // //             {
// // // //                 vis.insert({x + 1, y, z});
// // // //                 d.push({((ll)a[x + 1] * b[y] * c[z]), x + 1, y, z});
// // // //             }
// // // //             if (y + 1 < n && (vis.find({x, y + 1, z}) == vis.end()))
// // // //             {
// // // //                 vis.insert({x, y + 1, z});
// // // //                 d.push({((ll)a[x] * b[y + 1] * c[z]), x, y + 1, z});
// // // //             }
// // // //             if (z + 1 < n && (vis.find({x, y, z + 1}) == vis.end()))
// // // //             {
// // // //                 vis.insert({x, y, z + 1});
// // // //                 d.push({((ll)a[x] * b[y] * c[z + 1]), x, y, z + 1});
// // // //             }
// // // //         }

// // // //         for (int i = 0; i < m; i++)
// // // //             cout << ans[i] << ' ';

// // // //         cout << '\n';
// // // //     }
// // // //     return 0;
// // // // }

// // // // #include<bits/stdc++.h>

// // // // using namespace std;
// // // // using ll = long long;
// // // // int main( )
// // // // {
// // // //     int t, n, m;
// // // //     cin >> t;
// // // //     for(int i = 0; i< t; i++)
// // // //     {
// // // //         cin >> n >> m;
// // // //         vector<int> d(n);
// // // //         for(int j = 0; j < n ; j++)
// // // //         {
// // // //             cin >> d[j];
// // // //         }
// // // //         sort(d.begin(), d.end());
// // // //         ll ans = 0;
// // // //         vector<pair<int, int>> op;
// // // //         for(int j = 0; j < m; j++)
// // // //         {
// // // //             int t, z;
// // // //             cin >> t >> z;
// // // //             op.push_back({z, t});
// // // //         }
// // // //         sort(op.begin(), op.end());
// // // //         int cur = m - 1;
// // // //         for(int r = n - 1; r >= 0; r--)
// // // //         {
// // // //             if (d[r] <= op[cur].first && d[r] >= op[cur].second)
// // // //             {
// // // //                 ans += d[r];
// // // //                 cur++;
// // // //             }
// // // //         }

// // // //         cout << ans;
// // // //     }
// // // //     return 0;
// // // // }

// // // #include <bits/stdc++.h>

// // // using namespace std;
// // // using ll = long long;

// // // int main()
// // // {
// // //     int n, m;
// // //     cin >> n >> m;
// // //     vector<vector<int>> d(n + 1, vector<int>(m, 0));
// // //     map<int, int> mp;
// // //     for (int i = 1; i <= n; i++)
// // //     {
// // //         for (int j = 0; j < m; j++)
// // //         {
// // //             cin >> d[i][j];
// // //         }
// // //         mp[i] = i;
// // //     }

// // //     int q;
// // //     cin >> q;
// // //     for (int i = 0; i < q; i++)
// // //     {
// // //         int x, y;
// // //         cin >> x >> y;
// // //         int cur_x = mp[x];
// // //         int cur_y = mp[y];
// // //         mp[x] = cur_y;
// // //         mp[y] = cur_x;
// // //     }

// // //     for (auto [k, v] : mp)
// // //     {
// // //         for (int j = 0; j < m; j++)
// // //         {
// // //             cout << d[v][j] << ' ';
// // //         }
// // //         cout << '\n';
// // //     }
// // //     return 0;
// // // }

// // #include <bits/stdc++.h>
// // using namespace std;
// // using ll = long long;
// // int main()
// // {
// //     int t;
// //     cin >> t;
// //     for (int _ = 0; _ < t; _++)
// //     {
// //         int n;
// //         cin >> n;
// //         vector<int> d(n);
// //         for (int j = 0; j < n; j++)
// //         {
// //             cin >> d[j];
// //         }

// //         stack<int> ma;
// //         stack<int> mi;

// //         vector<int> l_ma(n, -1);
// //         vector<int> l_mi(n, -1);
// //         vector<int> r_ma(n, n);
// //         vector<int> r_mi(n, n);
// //         for (int i = 0; i < n; i++)
// //         {
// //             while (!ma.empty() && d[ma.top()] <= d[i])
// //             {
// //                 ma.pop();
// //             }
// //             while (!mi.empty() && d[mi.top()] >= d[i])
// //             {
// //                 mi.pop();
// //             }
// //             if (!ma.empty())
// //                 l_ma[i] = ma.top();

// //             if (!mi.empty())
// //                 l_mi[i] = mi.top();
// //             mi.push(i);
// //             ma.push(i);
// //         }
// //         while (!ma.empty())
// //             ma.pop();
// //         while (!mi.empty())
// //             mi.pop();

// //         for (int i = n - 1; i >= 0; i--)
// //         {
// //             while (!ma.empty() && d[ma.top()] < d[i])
// //             {
// //                 ma.pop();
// //             }
// //             while (!mi.empty() && d[mi.top()] > d[i])
// //             {
// //                 mi.pop();
// //             }
// //             if (!ma.empty())
// //                 r_ma[i] = ma.top();
// //             if (!mi.empty())
// //                 r_mi[i] = mi.top();
// //             mi.push(i);
// //             ma.push(i);
// //         }

// //         ll ans = 0;
// //         for (int i = 0; i < n; i++)
// //         {
// //             ll cur_mi = (ll)d[i] * (i - l_mi[i]) * (r_mi[i] - i);
// //             ll cur_ma = (ll)d[i] * (i - l_ma[i]) * (r_ma[i] - i);

// //             ans += cur_mi + cur_ma;
// //         }
// //         cout << ans << '\n';
// //     }
// //     return 0;
// // }

// // #include <bits/stdc++.h>
// // using ll = long long;
// // using namespace std;

// // int main()
// // {
// //     cin.tie(0)->sync_with_stdio(0);

// //     int n;
// //     cin >> n;
// //     vector<int> d(n);
// //     for (int i = 0; i < n; i++)
// //     {
// //         cin >> d[i];
// //     }
// //     vector<vector<int>> g(n + 1);
// //     for (int i = 0; i < n - 1; i++)
// //     {
// //         int x, y;
// //         cin >> x >> y;
// //         g[x].push_back(y);
// //         g[y].push_back(x);
// //     }
// //     cout << n;
// //     return 0;
// // }

// #include <bits/stdc++.h>
// using namespace std;
// using ll = long long;

// int main()
// {
//     string s;
//     cin >> s;
//     char c1, c2, c;
//     cin >> c1 >> c2;
//     string ans = "";
//     for (int i = 0; i < s.size();)
//     {
//         if (s[i] == c1)
//         {
//             for (int j = i + 1; j < s.size(); j++)
//             {
//                 if (s[j] == c2)
//                 {
//                     ans += s.substr(i + 1, j - i - 1);
//                     i = j;
//                     break;
//                 }
//             }
//         }
//         else
//             i++;
//     }
//     cout << ans;
// }

// #include <bits/stdc++.h>
// using namespace std;
// using ll = long long;

// int main()
// {
//     int a, b;
//     cin >> a >> b;
//     int f = 0;
//     int ans = 0;
//     for (int end = b; end >= a; end--)
//     {
//         for (int m = end - 1; m >= end / 2; m--)
//         {
//             int n = end - m;
//             if (int((n + 1.0) / m + (m + 1.0) / n) == ((n + 1.0) / m + (m + 1.0) / n))
//             {
//                 f = 1;
//                 ans = end;
//                 break;
//             }
//         }
//         if (f)
//             break;
//     }
//     if (f)
//         cout << ans;
//     else
//         cout << 0;
// }

// #include<bits/stdc++.h>
// using namespace std;
// using ll = long long;

// int main( )
// {
//     int n, q;
//     cin >> n >> q;
//     string s;
//     cin >> s;
//     vector<vector<int>> pre(n + 1, vector<int>(26, 0));
//     for(int i = 1; i <= n; i++)
//     {
//         pre[i][s[i-1] - 'a'] += pre[i-1][s[i-1] - 'a'];
//     }
//     for(int  i = 1; i <= q; i++)
//     {
//         int l, r;
//         cin >> l >> r;
//         int cnt = 26;
//         for(int j = 0; j < 26; j++)
//         {
//             if((pre[r][j] - pre[l - 1][j]) % 2)
//                 cnt--;
//         }
//         cout << cnt << ' ' << 26 - cnt << endl;
//     }
//     return 0;
// }

// #include <bits/stdc++.h>
// using ll = long long;
// using namespace std;
// const ll INF = 4e12;
// int main()
// {
//     int n, m, k;
//     cin >> n >> m >> k;
//     vector<vector<pair<int, ll>>> g(n + 1);

//     for (int i = 0; i < m; i++)
//     {
//         int u, v, w;
//         cin >> u >> v >> w;
//         g[u].push_back({v, w});
//         g[v].push_back({u, w});
//     }
//     vector<ll> dist(n + 1, INF);
//     priority_queue<
//         pair<ll, int>,
//         vector<pair<ll, int>>,
//         greater<pair<ll, int>>>
//         pq;

//     int k;
//     cin >> k;
//     ll ans = 0;
//     for (int i = 0; i < k; i++)
//     {
//         int p, t;
//         cin >> p >> t;
//         dist[p] = t;
//         pq.push({t, p});
//     }

//     while (!pq.empty())
//     {
//         auto [d, u] = pq.top();
//         pq.pop();
//         if (d > dist[u])
//             continue;
//         for (auto [v, w] : g[u])
//         {
//             if (dist[v] > dist[u] + w)
//             {
//                 dist[v] = dist[u] + w;
//                 pq.push({dist[v], v});
//             }
//         }
//     }

//     for (int i = 1; i <= n; i++)
//     {
//         ans = max(ans, dist[i]);
//     }
//     cout << ans;
//     return 0;
// }

#include <bits/stdc++.h>
using ll = long long;
using namespace std;
const ll mod = 1e9 + 7;
const ll N = 1e6 + 3;

int main()
{
    ll a, b;
    cin >> a >> b;
    cout << a + b;
    return 0;
}