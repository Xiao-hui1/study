#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll N = 1e5 + 5;
#define int ll
int a[N];
int lg[N];
int st[N][20];
int st_mi[N][20];

inline int read()
{
    int x = 0, f = 1;
    char ch = getchar();
    while (ch < '0' || ch > '9')
    {
        if (ch == '-')
            f = -1;
        ch = getchar();
    }
    while (ch >= '0' && ch <= '9')
    {
        x = x * 10 + ch - 48;
        ch = getchar();
    }
    return x * f;
}

void RMQ(int n)
{
    for (int i = 1; i <= n; i++)
        st[i][0] = st_mi[i][0] = a[i];

    for (int k = 1; k < 20; k++)
    {
        for (int i = 1; i + (1 << k) - 1 <= n; i++)
        {
            st[i][k] = max(st[i][k - 1], st[i + (1 << (k - 1))][k - 1]);
            st_mi[i][k] = min(st_mi[i][k - 1], st_mi[i + (1 << (k - 1))][k - 1]);
        }
    }
}

signed main()
{
    int n, m;
    n = read();
    m = read();

    for (int i = 1; i <= n; i++)
    {
        int t = read();
        a[i] = t;
    }
    lg[0] = -1;
    for (int i = 1; i <= n; i++)
        lg[i] = lg[i / 2] + 1;

    RMQ(n);

    for (int i = 0; i < m; i++)
    {
        int l, r, k, ans;
        l = read();
        r = read();
        k = lg[r - l + 1];

        int ma = max(st[l][k], st[r - (1 << k) + 1][k]);
        int mi = min(st_mi[l][k], st_mi[r - (1 << k) + 1][k]);

        ans = ma - mi;
        cout << ans << '\n';
    }

    return 0;
}