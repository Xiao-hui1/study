// #include <bits/stdc++.h>
// using namespace std;
// int main(){
//     string x, y;
//     vector<string> d = {"Ocelot", "Serval", "Lynx"};
//     cin >> x >> y;
//     if (find(d.begin(),d.end(), x) - d.begin() < find(d.begin(),d.end(), y) - d.begin()){
//         cout<<"No"<<endl;
//     }else
//         cout<<"Yes"<<endl;

//     return 0;
// }

// int main(){
//     string s;
//     cin >> s;
//     int a[26] = {0};
//     for(auto i: s){
//         a[i - 'a']++;
//     }
//     for(int i = 0; i < 26; i++)
//         if (a[i] == 1){
//             cout<<char('a' + i)<< endl;
//             break;
//         }
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;
// const int MAXN = 1e6 + 10;
// int val[MAXN];
// int maxv[MAXN << 2];
// int tag[MAXN << 2];
// typedef long long ll;
// typedef unsigned long long ull;
// typedef unsigned int ui;
// typedef long double ld;
// void pushup(int u){
//     maxv[u] = max(maxv[u << 1], maxv[u<<1 | 1]);
// }

// void build(int u, int l, int r){
//     tag[u] = 0;
//     if (l == r){
//         maxv[u] = val[l] = l;
//         return ;
//     }
//     int mid = (l + r) /2;
//     build(u << 1, l, mid);
//     build(u << 1 | 1, mid + 1, r);
//     pushup(u);
// }

// void pushdown(int u, int l, int r){
//     if (!tag[u]) return ;
//     int mid = (l + r) / 2;
//     int ls = u << 1, rs = u << 1 | 1;
//     maxv[ls] = tag[u];
//     tag[ls] = tag[u];
//     maxv[rs] = tag[u];
//     tag[rs] = tag[u];
//     tag[u] = 0;
// }

// int update(int u, int l, int r, int x, int y){
//     if (maxv[u] <= x){
//         int cnt = r - l + 1;
//         maxv[u] = y;
//         tag[u]= y;
//         return cnt;
//     }
//     if (l == r) return 0;
//     pushdown(u,l,r);
//     int mid = (l + r) /2;
//     int left = update(u << 1, l, mid , x,y);
//     int right = update(u<<1|1,mid + 1, r, x,y);
//     pushup(u);
//     return left + right;
// }

// int main(){
//     ios::sync_with_stdio(false);
//     cin.tie(0);
//     ll n,q, max_x = 0, max_y = 0;
//     ll x, y;
//     cin >> n >> q;
//     build(1,1,n);
//     for(ll i = 0; i < q; i++){
//         cin >> x >> y;
//         cout << update(1, 1, n, x, y)<<endl;
//     }

//     return 0;
// }

// #include <iostream>
// #include <set>
// #include <vector>
// using namespace std;

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);

//     int N, Q;
//     cin >> N >> Q;

//     vector<long long> cnt(N + 1, 0);
//     set<int> exist;

//     for (int i = 1; i <= N; ++i) {
//         cnt[i] = 1;
//         exist.insert(i);
//     }

//     while (Q--) {
//         int X, Y;
//         cin >> X >> Y;

//         long long upgraded = 0;
//         vector<int> to_remove;

//         for (auto it = exist.begin(); it != exist.end() && *it <= X; ++it) {
//             int version = *it;
//             upgraded += cnt[version];
//             cnt[Y] += cnt[version];
//             to_remove.push_back(version);
//         }

//         for (int version : to_remove) {
//             exist.erase(version);
//             cnt[version] = 0;
//         }

//         cout << upgraded << '\n';
//     }

//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;
// typedef long long ll;
// int main()
// {
//     double a, b;
//     cin >> a >> b;
//     string res = "";
//     for (int i = 0; i < 50; ++i)
//     {
//         if (b > 0.5)
//         {
//             res += '2';
//             b = 2.0 * b - 1.0;
//         }
//         else
//         {
//             res += '1';
//             b = 2.0 * b;
//         }
//         if (a == b)
//             break;
//     }
//     reverse(res.begin(), res.end());
//     cout << res;
//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    set<int> d;
    const int N = 1e6 + 1;
    vector<int> d_a(N), d_b(N), d_c(N);
    int a, b, c;
    cin >> a >> b >> c;

    for (int i = 0; i < a; i++)
        cin >> d_a[i];

    for (int i = 0; i < b; i++)
    {
        cin >> d_b[i];
        for (int j = 0; j < a; j++)
            d.insert(d_b[i] + d_a[j]);
    }

    for (int i = 0; i < c; i++)
        cin >> d_c[i];

    sort(d_c.begin(), d_c.end());

    if (d.size() != c)
        cout << "NO";
    else
    {
        int f = 1;
        auto it = d.begin();
        for (auto &i : d_c)
        {
            if (*it != i)
            {
                f = 0;
                break;
            }
            it++;
        }
        if (f)
            cout << "YES";
        else
            cout << "NO";
    }
    return 0;
}