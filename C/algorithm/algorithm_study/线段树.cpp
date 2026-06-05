#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define int long long
#define N 1000001
// #define M static_cast<int>(1e6)
constexpr const ll M = 1e6;

ll a[M];

struct node
{
    int val;
    int l;
    int r;
    ll sum = 0;
    int lazy = 0;
};

vector<node> d(N * 4);
vector<int> da(N, 0);

void build(int pos, int l, int r)
{
    d[pos].l = l;
    d[pos].r = r;
    if (l == r)
    {
        d[pos].sum = da[l];
        return;
    }
    int mid = (l + r) / 2;
    build(pos << 1, l, mid);
    build(pos << 1 | 1, mid + 1, r);
    d[pos].sum = d[pos << 1].sum + d[pos << 1 | 1].sum;
}

void push_lazy(int x)
{
    if (d[x].lazy)
    {
        d[x * 2].lazy += d[x].lazy;
        d[x * 2].sum += d[x * 2].lazy * (d[x * 2].r - d[x * 2].l + 1);
        d[x * 2 | 1].lazy += d[x].lazy;
        d[x * 2 | 1].sum += d[x * 2 | 1].lazy * (d[x * 2 | 1].r - d[x * 2 | 1].l + 1);
        d[x].lazy = 0;
    }
}

void update(int l, int r, int k, int x)
{
    if (d[x].r == r && d[x].l == l)
    {
        d[x].sum += k * (d[x].r - d[x].l + 1);
        d[x].lazy += k;
        return;
    }
    push_lazy(x);
    int mid = (d[x].l + d[x].r) >> 1;
    if (r <= mid)
        update(l, r, k, x << 1);
    else if (l > mid)
        update(l, mid, k, x << 1 | 1);
    else
    {
        update(l, mid, k, x << 1);
        update(mid + 1, r, k, x << 1 | 1);
    }
    d[x].sum = d[x * 2].sum + d[x * 2 | 1].sum;
}

ll query(int l, int r, int x)
{
    if (d[x].r == r && d[x].l == l)
        return d[x].sum;
    push_lazy(x);
    int mid = (d[x].r + d[x].l) >> 1;
    if (r <= mid)
        return query(l, r, x * 2);
    else if (l > mid)
        return query(l, r, x * 2 | 1);
    else
        return query(l, mid, x << 1) + query(mid + 1, r, x << 1 | 1);
}

int main()
{
    int n, q, op, x, y, k;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> da[i];
    }
    build(1, 1, n);
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        cin >> op;
        if (op == 1)
        {
            cin >> x >> y >> k;
            update(x, y, k, 1);
        }
        else
        {
            cin >> x >> y;
            cout << query(x, y, 1) << endl;
        }
    }
    return 0;
}