#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll N = 1e6 + 3;
ll dp[N][3];
const ll mod = 1e9 + 7;
// void solve(int ma)
// {
//     dp[1][0] = 1;
//     dp[2][1] = 1;
//     for (int i = 3; i <= ma; i++)
//     {
//         dp[i][2] = ((dp[i - 2][2] + dp[i - 1][2]) % mod + (dp[i - 2][1] * dp[i - 1][0]) % mod) % mod;
//         dp[i][0] = (dp[i - 2][0] + dp[i - 1][0]) % mod;
//         dp[i][1] = (dp[i - 2][1] + dp[i - 1][1]) % mod;
//     }
// }

ll mi_l[N], max_l[N], mi_r[N], max_r[N];

stack<ll> st;

int main()
{
    ll n;
    cin >> n;
    vector<ll> d(n);
    for (int i = 0; i < n; i++)
    {
        cin >> d[i];
    }

    for (int i = 0; i < n; i++)
    {
        while (!st.empty() && d[st.top()] > d[i])
        {
            st.pop();
        }
        if (st.empty())
        {
            mi_l[i] = -1;
        }
        else
            mi_l[i] = st.top();
        st.push(i);
    }

    while (!st.empty())
        st.pop();

    for (ll i = 0; i < n; i++)
    {
        while (!st.empty() && d[st.top()] < d[i])
        {
            st.pop();
        }
        if (st.empty())
        {
            max_l[i] = -1;
        }
        else
            max_l[i] = st.top();
        st.push(i);
    }
    while (!st.empty())
        st.pop();

    for (int i = n - 1; i >= 0; i--)
    {
        while (!st.empty() && d[st.top()] >= d[i])
        {
            st.pop();
        }
        if (st.empty())
        {
            mi_r[i] = n;
        }
        else
            mi_r[i] = st.top();
        st.push(i);
    }
    while (!st.empty())
        st.pop();

    for (int i = n - 1; i >= 0; i--)
    {
        while (!st.empty() && d[st.top()] <= d[i])
        {
            st.pop();
        }
        if (st.empty())
        {
            max_r[i] = n;
        }
        else
            max_r[i] = st.top();
        st.push(i);
    }

    ll ans = 0;
    for (int i = 0; i < n; i++)
    {
        ans += (i - max_l[i]) * (max_r[i] - i) * d[i];
        ans -= ((i - mi_l[i]) * (mi_r[i] - i) * d[i]);
    }
    cout << ans;
    return 0;
}