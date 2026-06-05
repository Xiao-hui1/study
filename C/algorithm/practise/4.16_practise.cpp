// // // #include <iostream>
// // // using namespace std;
// // // int main(){
// // //     string s;
// // //     cin>> s;
// // //     int l, mid;
// // //     l = s.length();
// // //     mid = (l + 1) / 2;
// // //     for(int i = 1; i <= l; i++){
// // //         if (i != mid){
// // //             cout<<s[i-1];
// // //         }
// // //     }
// // //     return 0;
// // // }

// // // #include <bits/stdc++.h>
// // // using namespace std;
// // // int fun(int a){
// // //     long long su = 0;
// // //     while (a){
// // //         su += a % 10;
// // //         a /= 10;
// // //     }
// // //     return su;
// // // }

// // // int main(){
// // //     vector<int> d(101, 1);
// // //     int n;
// // //     cin >> n;
// // //     for(int i = 2; i <= n;i++){
// // //         d[i] = d[i - 1] + fun(d[i - 1]);
// // //     }
// // //     cout << d[n];
// // //     return 0;
// // // }

// // // #include <iostream>
// // // #include <vector>
// // // #include <algorithm>
// // // using namespace std;

// // // int main() {
// // //     int N, M;
// // //     cin >> N >> M;

// // //     vector<pair<int, int>> edges;
// // //     for (int i = 0; i < M; i++) {
// // //         int u, v;
// // //         cin >> u >> v;
// // //         edges.push_back({u, v});
// // //     }

// // //     int min_deletions = M;

// // //     for (int mask = 0; mask < (1 << N); mask++) {
// // //         int deletions = 0;

// // //         for (auto& edge : edges) {
// // //             int u = edge.first - 1;
// // //             int v = edge.second - 1;

// // //             if (((mask >> u) & 1) == ((mask >> v) & 1)) {
// // //                 deletions++;
// // //             }
// // //         }

// // //         min_deletions = min(min_deletions, deletions);
// // //     }

// // //     cout << min_deletions << endl;

// // //     return 0;
// // // }

// // // #include <bits/stdc++.h>
// // // using namespace std;
// // // #define ll long long;
// // // int main(){
// // //     int n ,m;
// // //     cin >> n >> m;
// // //     vector<vector<int>> d(n, vector<int> (n,1));
// // //     vector<string> da(n);
// // //     for(int i = 0; i < n; i++)
// // //         cin >> da[i];
// // //     for(int i = 0; i< n; i++)
// // //         for(int j = 0; j< n; j++)
// // //             if (da[i][j] == '#')
// // //                 d[i][j] = 2;
// // //     map<std::tuple<int, int, int, int>,int> ans;
// // //     for(int i = 0; i < n - m; i++)
// // //         for(int j = 1; j < n; j++)

// // //     return 0;
// // // }

// // // #include <bits/stdc++.h>
// // // using namespace std;
// // // typedef long long ll;
// // // int main(){
// // //     int n, a, b;
// // //     cin>> n >> a>>b;
// // //     string s;
// // //     cin>> s;
// // //     vector<int> pre_a(n + 1, 0);
// // //     vector<int> pre_b(n + 1, 0);
// // //     for(int i = 1; i <= n; i++){
// // //         pre_a[i] += pre_a[i - 1] + (s[i-1] == 'a');
// // //         pre_b[i] += pre_b[i - 1] + (s[i -1] == 'b');
// // //     }
// // //     int l = 1;
// // //     ll ans = 0;
// // //     for(ll r = 1; r <= n; r++){
// // //         while(l <= r && pre_b[r] - pre_b[l - 1] >= b){
// // //             l += 1;
// // //         }
// // //         if(l < r && pre_a[r] - pre_a[l - 1] >= a && r - 1 >= 0 && pre_b[r - 1] - pre_b[l - 1] < b){
// // //             ans += pre_a[r] - pre_a[l - 1] - a + 1;
// // //         }
// // //     }
// // //     cout << ans << endl;
// // //     return 0;
// // // }

// // #include<bits/stdc++.h>
// // using namespace std;
// // #define int long long
// // int n, ans, dis[500005];
// // set<int> s = {0};
// // map<int,int> h;

// // void upd(int p, bool f) {
// //     if (f)
// //         ans -= dis[h[p]];
// //     auto it = s.find(p);
// //     if (p != 0)
// //         dis[h[p]] = min(dis[h[p]], p - *(--it)), ++it;
// //     if (++it != s.end())
// //         dis[h[p]] = min(dis[h[p]], *it - p);
// //     ans += dis[h[p]];
// // }

// // signed main() {
// //     cin >> n;
// //     memset(dis, 0x3f, sizeof dis);
// //     ans = dis[0];
// //     h[0] = 0;
// //     for (int i = 1; i <= n; i++) {
// //         int x;
// //         cin >> x;
// //         h[x] = i;
// //         s.insert(x);
// //         upd(x, 0);
// //         auto it = s.find(x);
// //         upd(*(--it), 1), ++it;
// //         if (++it != s.end())
// //             upd(*it, 1);
// //         cout << ans << endl;
// //     }
// //     return 0;
// // }

// // // #include<bits/stdc++.h>
// // // #define re ree()
// // // #define debug(x) cout<<'\n'<<#x<<':'<<x<<'\n';
// // // using namespace std;
// // // long long ree()																										{long long x=0,f=1;char c=0;while(c<'0'||c>'9'){if(c=='-')f=-1;c=getchar();}while(c>='0'&&c<='9'){x=(x<<3)+(x<<1)+(c-'0');c=getchar();}return x*f;}
// // // long long n,ans,a,b,f[1000100],l,r,suma[1000100],sumb[1000100];
// // // string s;
// // // int main()
// // // {
// // // 	n=re;
// // // 	a=re;
// // // 	b=re;
// // // 	cin>>s;
// // // 	for(int i=0;i<s.size();i++)
// // // 	{
// // // 		suma[i+1]=suma[i];
// // // 		sumb[i+1]=sumb[i];
// // // 		if(s[i]=='a')
// // // 		{
// // // 			suma[i+1]++;
// // // 		}
// // // 		else
// // // 		{
// // // 			sumb[i+1]++;
// // // 		}
// // // 	}
// // // 	for(int i=1;i<=n;i++)
// // // 	{
// // // 		while(sumb[i]-sumb[l]>=b&&l<i)
// // // 		{
// // // 			l++;
// // // 		}
// // // 		while(suma[i]-suma[r]>=a&&r<i)
// // // 		{
// // // 			r++;
// // // 		}
// // // 		if(r-l>0)
// // // 		{
// // // 			ans+=r-l;
// // // 		}
// // // 	}
// // // 	cout<<ans;
// // // 	return 0;
// // // }

// // #include <bits/stdc++.h>
// // using namespace std;
// // const int N = 1e+6;
// // typedef long long ll;
// // int main(){
// //     ll n, m , k , f = 1, cnt = 0;
// //     ios::sync_with_stdio(false);
// //     cin.tie(0);
// //     cin >> n >> m >> k;
// //     vector<int> head(n, 0);
// //     vector<int> body(m, 0);
// //     for(int i = 0; i < n; i++)
// //         cin>>head[i];
// //     for(int i = 0; i < m; i++)
// //         cin>>body[i];
// //     sort(head.begin(), head.begin() + n);
// //     reverse(body.begin(), body.begin() + m);
// //     if (min(n, m) < k)
// //         cout << "No";
// //     else
// //         if(m <= n){
// //             for(int i = 0; i < m; i++){
// //                 if(cnt == k){
// //                     break;
// //                 }
// //                 cnt += 1;
// //             }
// //         }else{
// //             for(int i = 0; i < n; i++){
// //                 if(cnt == k){
// //                     break;
// //                 }
// //                 cnt++;
// //             }
// //         }
// //         if (cnt >= k)
// //             cout << "Yes";
// //         else
// //             cout << "No";
// //     return 0;
// // }

// // 背包dp
// //  #include<bits/stdc++.h>
// //  #define ll long long
// //  using namespace std;
// //  const int N = 505;
// //  ll w[N],h[N],b[N],dp[N*N];
// //  ll n,m,sum,ans;
// //  int main(){
// //  	cin>>n;
// //  	for(int i=1;i<=n;i++){
// //  		cin>>w[i]>>h[i]>>b[i];
// //  		sum+=w[i];
// //  		ans+=b[i];
// //  	}
// //  	m=sum/2;
// //  	for(int i=1;i<=n;i++){
// //  		for(int j=m;j>=w[i];j--)
// //  			dp[j]=max(dp[j],dp[j-w[i]]+(h[i]-b[i]));
// //  	}
// //  	cout<<ans+dp[m];
// //  	return 0;
// //  }

// // #include <bits/stdc++.h>
// // using namespace std;
// // typedef long long ll;
// // int main(){
// //     vector <int> a(20, 1e6);
// //     string s;
// //     cin >> s;
// //     int i = 0;
// //     int l = s.length();
// //     if (l == 1)
// //         cout << s;
// //     else{
// //         int cnt = 0;
// //         for(auto x :s){
// //             a[i] = x - '0';
// //             cnt += !(x - '0');
// //             i ++;
// //         }
// //         sort(a.begin(), a.end());
// //         ll ans = 0;
// //         if (cnt){
// //             ans = a[cnt] * pow(10, cnt);
// //             for (int i = cnt + 1; i < l; i++)
// //                 ans = ans * 10 + a[i];
// //         }else
// //             for(int i = 0; i < l; i++)
// //                 ans = ans * 10 + a[i];
// //         cout<< ans;
// //     }

// //     return 0;
// // }

// // #include <bits/stdc++.h>
// // using namespace std;
// // typedef long long ll;
// // int main(){
// //     stack<int> d;
// //     int n;
// //     cin >> n;
// //     int data[102], res[102] = {0};
// //     for(int i = 0; i < n; i++){
// //         cin >> data[i];
// //     }
// //     int i = 0;
// //     for(auto x: data){
// //         while(!d.empty() && data[d.top() - 1] <= x){
// //             d.pop();
// //         }
// //         if (!d.empty()){
// //             res[i++] = d.top();
// //         }else
// //             res[i++] = -1;
// //         d.push(i);
// //     }
// //     for(int i = 0; i < n; i++)
// //         cout<< res[i]<<endl;
// //     return 0;
// // }

// // #include<bits/stdc++.h>
// // #define LL long long
// // using namespace std;
// // const int N = 2e5+5;
// // LL n,m,a[N],len[N],Ans;
// // map<LL,LL> mp[12];
// // LL read(){
// //     LL su=0,pp=1;char ch=getchar();
// //     while(ch<'0'||ch>'9'){if(ch=='-')pp=-1;ch=getchar();}
// //     while(ch>='0'&&ch<='9'){su=su*10+ch-'0';ch=getchar();}
// //     return su*pp;
// // }
// // LL LEN(LL x){LL c=0;while(x)c++,x/=10;return c;}
// // int main(){
// //     n=read(),m=read();
// //     for(int i=1;i<=n;i++)
// //         a[i]=read(),len[i]=LEN(a[i]);
// //     for(int i=1;i<=n;i++)
// //         for(LL j=1,x=10;j<=10;j++,x=(x*10)%m)
// //             mp[j][(a[i]*x)%m]++;
// //     for(int i=1;i<=n;i++)
// //         Ans+=mp[len[i]][(m-(a[i]%m))%m];
// //     cout<<Ans<<"\n";
// //     return 0;
// // }

// // #include <bits/stdc++.h>
// // using namespace std;
// // int main()
// // {
// //     int n;
// //     cin >> n;
// //     cout << ((1 + n) * n) / 2;
// //     return 0;
// // }

// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);

//     int N, M;
//     cin >> N >> M;

//     vector<vector<int>> graph(N + 1);
//     for (int i = 0; i < M; i++) {
//         int x, y;
//         cin >> x >> y;
//         graph[x].push_back(y);
//     }

//     int Q;
//     cin >> Q;

//     vector<bool> is_black(N + 1, false);

//     while (Q--) {
//         int type, v;
//         cin >> type >> v;

//         if (type == 1) {
//             is_black[v] = true;
//         } else {
//             if (is_black[v]) {
//                 cout << "Yes\n";
//                 continue;
//             }

//             vector<bool> visited(N + 1, false);
//             queue<int> q;
//             q.push(v);
//             visited[v] = true;
//             bool found = false;

//             while (!q.empty() && !found) {
//                 int curr = q.front();
//                 q.pop();

//                 for (int next : graph[curr]) {
//                     if (is_black[next]) {
//                         found = true;
//                         break;
//                     }
//                     if (!visited[next]) {
//                         visited[next] = true;
//                         q.push(next);
//                     }
//                 }
//             }

//             cout << (found ? "Yes\n" : "No\n");
//         }
//     }

//     return 0;
// }

// // #include <bits/stdc++.h>
// // using namespace std;
// // int main()
// // {
// //     int n;
// //     cin >> n;
// //     int v;
// //     string s;
// //     for (int i = 0; i < n; i++)
// //     {
// //         cin >> s;
// //         stack<int> d;
// //         int r = 0, l = 0;
// //         for (auto c : s)
// //         {
// //             if (c == '(')
// //                 d.push('(');
// //             else
// //                 d.pop();
// //         }
// //     }

// //     return 0;
// // }

// #include <bits/stdc++.h>
// using namespace std;
// typedef long long ll;
// int main()
// {
//     int n;
//     cin >> n;
//     int x, y, pos_x, pos_y;
//     char dir;
//     for (int i = 0; i < n; i++)
//     {
//         cin >> x >> y >> dir >> pos_x >> pos_y;
//         int dx = pos_x - x;
//         int dy = pos_y - y;
//         if (dx == 0 && dy == 0)
//         {
//             cout << 0 << endl;
//             continue;
//         }

//         vector<int> direct;
//         if (dy > 0)
//             direct.push_back(0);
//         if (dx > 0)
//             direct.push_back(1);
//         if (dy < 0)
//             direct.push_back(2);
//         if (dx < 0)
//             direct.push_back(3);

//         int ans = 1e9, dirc = 0;

//         if (dir == 'E')
//             dirc = 1;
//         else if (dir == 'S')
//             dirc = 2;
//         else if (dir == 'W')
//             dirc = 3;

//         if (direct.size() == 1)
//         {
//             ans = (direct[0] - dirc + 4) % 4;
//         }
//         else
//         {
//             int a = direct[0], b = direct[1];
//             int t1 = (a - dirc + 4) % 4 + (b - a + 4) % 4;
//             int t2 = (b - dirc + 4) % 4 + (a - b + 4) % 4;
//             ans = min(t1, t2);
//         }
//         cout << ans << endl;
//     }
//     return 0;
// }
