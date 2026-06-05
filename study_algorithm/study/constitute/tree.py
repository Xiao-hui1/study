n = int(input())

dp = [[]]*(n+1)
st = [0] * (n+1)

for i in range(n):
    x, y = map(int, input().split())
    #创建的无向树
    dp[x].append(y)
    dp[y].append(x)

def dfs(x):
    print(x)
    st[x] = 1
    for i in dp[x]:
        if not st[i]:
            dfs(i)
dfs(1)

id = 0
h = [0] * (n + 1)
e = [0] * (n * 2 + 1)
ne = [0] * (n * 2 + 1)
#使用链式前向星创建树

def add(x, y):
    global id
    id += 1
    e[id] = y
    ne[id] = h[x]
    h[x] = id