n = int(input())
p = 131
mod = 10**9 + 7
res = []

for _ in range(n):
    val = input()
    ret = 0
    size = len(val)
    for i in range(0, size):
        ret = (ret * p + ord(val[i])) % mod
    res.append(ret)

count = 0
res.sort()
for i in range(n):
    if i == 0 or res[i] != res[i - 1]:
        count += 1
print(count)