n = int(input())
p = 3
res = []

for _ in range(n):
    val = input()
    ret = 0
    size = len(val)
    for i in range(0, size):
        ret = ret * p + ord(val[i])
    res.append(ret)

count = 1
res.sort()
for i in range(1, n):
    if res[i] != res[i-1]:
        count += 1
print(count)