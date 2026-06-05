m, n = list(map(int, input().split()))
cnt = 0
dp = [[] for i in range(n+1)]
for i in range(n):
    da = list(map(int, input().split()))
    cnt = max(cnt, da[2])
    dp[da[2]].append((da[0],da[1]))

f = [[0]*(m+1) for _ in range(cnt+1)]
for i in range(1,cnt+1):
    j = m
    while j >= 0:
        f[i][j] = f[i-1][j]
        for t in dp[i]:
            a = t[0]
            b = t[1]
            if j >= a:
                f[i][j] = max(f[i][j], f[i-1][j - a] + b)
        j -= 1
print(f[cnt][m])