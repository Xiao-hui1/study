s = ' ' + input()
dp = [[0]*(len(s)+1) for _ in range(len(s)+1)]
n = len(s) - 1
for len in range(2,n+1):
    i = 1
    while i + len - 1 <= n:
        j = i + len - 1
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1]
        else:
            dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        i += 1

print(dp[1][n])
