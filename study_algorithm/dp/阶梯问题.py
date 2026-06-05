n, k = list(map(int, input().split()))

dp = [1] + [0] * n

for i in range(1, k+1):
    dp[i] = sum(dp[:i])

for i in range(k+1, n+1):
    dp[i] = sum(dp[i-k:i]) % 100003
print(dp[n])