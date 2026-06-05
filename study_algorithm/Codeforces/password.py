size = int(input())
res = []
for x in range(size):
    l = int(input())
    dp = [0 for _ in range(l)]
    val = list(map(int, input().split()))
    for i in range(1,l):
        dp[i] = abs(val[i] - val[i-1]) + abs(val[i+1] - val[i])
    ma = 0
    for i in range(1,l):
        if dp[ma] < dp[i]:
            ma = i
    val.pop(ma)
    sum = 0
    for j in range(l - 2):
        sum += abs(val[j+1] - val[j])
    res.append(sum)
for i in res:
    print(i)

# size = int(input())
# res = []
# for i in range(size):
#     k,x = map(int, input().split())
#     res.append(k * x + 1)
#
# for i in range(size):
#     print(res[i])