n = int(input())

val = list(map(int, input().split()))
data = sorted([[v,i+1] for i, v in enumerate(val)], key = lambda x: x[0])
res = [i[1] for i in data]
total = 0
val = [0] * n
for i in range(1, n):
    val[i] = val[i-1] + data[i - 1][0]
total = sum(val) / n
print(*res)
print(f"{total:.2f}")