n , m, t = map(int, input().split())
dp = [[0] * (t + 1) for _ in range(m + 1)]
for _ in range(n):
    x,y = map(int, input().split())
    for i in range(m, x - 1, -1):
        for j in range(t, y - 1, -1):
            dp[i][j] = max(dp[i][j], dp[i - x][j - y] + 1)
print(max(max(row for row in dp)))