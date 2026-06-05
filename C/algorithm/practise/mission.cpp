// // #include <bits/stdc++.h>
// // using namespace std;

// // const int N = 1005;

// // int H, W;
// // string grid[N];
// // int dist[N][N];

// // vector<pair<int, int>> pos[26];
// // bool used[26];

// // int dx[4] = {1, -1, 0, 0};
// // int dy[4] = {0, 0, 1, -1};

// // int main()
// // {
// //     ios::sync_with_stdio(false);
// //     cin.tie(nullptr);

// //     cin >> H >> W;

// //     for (int i = 0; i < H; i++)
// //     {
// //         cin >> grid[i];
// //     }

// //     for (int i = 0; i < H; i++)
// //     {
// //         for (int j = 0; j < W; j++)
// //         {
// //             if (isalpha(grid[i][j]))
// //             {
// //                 pos[grid[i][j] - 'a'].push_back({i, j});
// //             }
// //         }
// //     }

// //     for (int i = 0; i < H; i++)
// //     {
// //         for (int j = 0; j < W; j++)
// //         {
// //             dist[i][j] = -1;
// //         }
// //     }

// //     queue<pair<int, int>> q;
// //     q.push({0, 0});
// //     dist[0][0] = 0;

// //     while (!q.empty())
// //     {
// //         auto [x, y] = q.front();
// //         q.pop();

// //         if (x == H - 1 && y == W - 1)
// //         {
// //             cout << dist[x][y] << '\n';
// //             return 0;
// //         }

// //         for (int k = 0; k < 4; k++)
// //         {
// //             int nx = x + dx[k];
// //             int ny = y + dy[k];

// //             if (nx < 0 || nx >= H || ny < 0 || ny >= W)
// //                 continue;
// //             if (grid[nx][ny] == '#')
// //                 continue;
// //             if (dist[nx][ny] != -1)
// //                 continue;

// //             dist[nx][ny] = dist[x][y] + 1;
// //             q.push({nx, ny});
// //         }

// //         char c = grid[x][y];
// //         if (isalpha(c))
// //         {
// //             int id = c - 'a';

// //             if (!used[id])
// //             {
// //                 used[id] = true;

// //                 for (auto [nx, ny] : pos[id])
// //                 {
// //                     if (dist[nx][ny] == -1)
// //                     {
// //                         dist[nx][ny] = dist[x][y] + 1;
// //                         q.push({nx, ny});
// //                     }
// //                 }
// //             }
// //         }
// //     }

// //     cout << -1 << '\n';
// //     return 0;
// // }

// // #include <bits/stdc++.h>
// // using namespace std;
// // #define int long long
// // int t;
// // struct edge
// // {
// //     int a, b;
// // } f[300005];
// // bool cmp(edge x, edge y)
// // {
// //     return x.a + x.b > y.a + y.b;
// // }
// // signed main()
// // {
// //     cin >> t;
// //     while (t--)
// //     {
// //         int n;
// //         cin >> n;
// //         int h = 0, c = 0;
// //         for (int i = 1; i <= n; i++)
// //         {
// //             cin >> f[i].a >> f[i].b;
// //             h += f[i].a;
// //         }
// //         sort(f + 1, f + n + 1, cmp);
// //         bool flag = 0;
// //         for (int i = 1; i <= n; i++)
// //         {
// //             if (c >= h)
// //             {
// //                 cout << n - (i - 1) << endl;
// //                 flag = 1;
// //                 break;
// //             }
// //             else
// //             {
// //                 h -= f[i].a;
// //                 c += f[i].b;
// //             }
// //         }
// //         if (!flag)
// //             cout << 0 << endl;
// //     }
// //     return 0;
// // }

// #include <bits/stdc++.h>
// using namespace std;
// typedef long long ll;
// const long long MOD = 998244353;

// int main()
// {
//     ios_base::sync_with_stdio(false);
//     cin.tie(NULL);

//     int N, M;
//     cin >> N >> M;

//     vector<ll> A(N);
//     vector<ll> B(M);

//     for (int i = 0; i < N; ++i)
//         cin >> A[i];
//     for (int i = 0; i < M; ++i)
//         cin >> B[i];

//     sort(A.begin(), A.end());

//     vector<ll> prefix_sum(N + 1, 0);
//     for (int i = 0; i < N; ++i)
//     {
//         prefix_sum[i + 1] = (prefix_sum[i] + A[i]) % MOD;
//     }

//     ll total_ans = 0;

//     for (int i = 0; i < M; ++i)
//     {
//         ll b = B[i];

//         int k = lower_bound(A.begin(), A.end(), b) - A.begin();

//         ll smaller_part = ((b % MOD) * (k % MOD)) % MOD;
//         smaller_part = (smaller_part - prefix_sum[k] + MOD) % MOD;

//         ll sum_larger = (prefix_sum[N] - prefix_sum[k] + MOD) % MOD;
//         ll count_larger = N - k;

//         ll larger_part = (sum_larger - ((b % MOD) * (count_larger % MOD)) % MOD + MOD) % MOD;

//         total_ans = (total_ans + smaller_part + larger_part) % MOD;
//     }

//     cout << total_ans << endl;

//     return 0;
// }

// #include <iostream>
// #include <vector>
// #include <algorithm>
// #include <numeric>

// using namespace std;

// int main()
// {
//     ios_base::sync_with_stdio(false);
//     cin.tie(NULL);

//     int N;
//     cin >> N;

//     vector<vector<int>> A(N + 1);

//     for (int i = 1; i <= N; ++i)
//     {
//         int x, y;
//         cin >> x >> y;
//         A[i] = A[x];
//         A[i].push_back(y);
//     }

//     vector<int> P(N);
//     iota(P.begin(), P.end(), 1);

//     sort(P.begin(), P.end(), [&](int i, int j)
//          {
//         if (A[i] != A[j]) {
//             return A[i] < A[j];
//         }
//         return i < j; });

//     for (int i = 0; i < N; ++i)
//     {
//         cout << P[i] << " ";
//     }
//     cout << endl;

//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int x, y;
        cin >> x >> y;
        int cnt = 1;
        for (int j = 1; j < y; j++)
        {
            if (y % j == 0)
                cnt++;
        }
        if (cnt % 2)
            cout << "YES";
        else
            cout << "NO";
    }
    return 0;
}