#树状数组实现：
n, p = map(int, input().split())
a = [0] + list(map(int, input().split()))
c = [0 for _ in range(n + 1)]

def lowbit(i):
    return (-i) & i

def update(i, k):
    j = i
    while j <= n:
        c[j] += k
        j += lowbit(j)

def pre_sum(i):
    s = 0
    while i > 0:
        s += c[i]
        i -= lowbit(i)
    return s

def get_sum(l, r):
    return pre_sum(r) - pre_sum(l - 1)

for i in range(1, n + 1):
    update(i, a[i])

for i in range(p):
    da = list(map(int, input().split()))
    if da[0] == 1:
        i, k = da[1], da[2]
        update(i, k)
    else:
        l, r = da[1], da[2]
        print(get_sum(l, r))