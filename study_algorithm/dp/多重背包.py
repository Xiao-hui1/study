n, m = list(map(int, input().split()))
s =[]
v = []
w = []
dp = [[0]* (n+1) for i in range(n+1)]
for i in range(n):
    da = list(map(int, input().split()))
    s.append(da[0])
    v.append(da[1])
    w.append(da[2])
for i in range(1, n+1):
    for j in range(1, n + 1):
        k = 0
        while k <= s[i] and k * v[i] <= j:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - k * v[i]]+ k * w[i])
            k += 1
print(dp[n][m])


#利用二进制进行优化

dp = [0] * (n * 5)
n, m = list(map(int, input().split()))
s =[]
v = []
w = []
pos = 0
for i in range(n):
    da = list(map(int, input().split()))
    s.append(da[0])
    v.append(da[1])
    w.append(da[2])
    t = 1
    while s[-1] >= t:
        pos += 1
        v[pos] = t * v[-1]
        w[pos] = t * w[-1]
        s[-1] -= t
        t *= 2
    if s[-1]:
        pos += 1
        v[pos] = s[-1] * v[-1]
        w[pos] = s[-1] * w[-1]
for i in range(1, pos+1):
    j = m
    while j >= v[i]:
        dp[j] = max(dp[j], dp[j-v[i] + w[i]])
        j -= 1

print(dp[m])