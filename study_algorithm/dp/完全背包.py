n , m= list(map(int, input().split()))
v = []
w = []
for i in range(n):
    s = list(map(int, input().split()))
    v.append(s[0])
    w.append(s[1])

dp = [[0]*(n+1)]*(n+1)
for i in range(1, n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j]
        if j >= v[i]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-v[i]]+w[i])

print(dp[n][m])

dp = [[float('inf')]*(n+1)]*(n+1)
for i in range(1, n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j]
        if j >= v[i]:
            #dp[i][j-v[i]]+w[i] 此为状态优化的方程
            dp[i][j] = max(dp[i-1][j], dp[i][j-v[i]] + w[i])

print(dp[n][m] if dp[n][m] != float('inf') else 0)