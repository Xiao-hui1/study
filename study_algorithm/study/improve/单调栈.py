
#单调栈用于快速求出，当前位置左边或右边的第一个距离最近，而且大于当前值的位置

n = int(input())
val = [0] + list(map(int, input().split()))
li = []
res = [-1] * n

for i in range(n, 0, -1):
    while len(li) and val[li[-1]] <= val[i]:
        li.pop()
    if li:
        res[i-1] = li[-1]
    li.append(i)

print(*res)