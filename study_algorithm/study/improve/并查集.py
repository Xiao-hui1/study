# n , m = list(map(int, input().split()))
# f = [i for i in range(1, n+1)]
# def find(x):
#     if x != f[x-1]:
#         f[x-1] = find(f[x-1])
#     return f[x-1]
#
# def Union(x, y):
#     a = find(x)
#     b = find(y)
#     if a < b:
#         f[b - 1] = a
#
# for i in range(m):
#     x, y = list(map(int, input().split()))
#     Union(x, y)
# ans = 0
# for i in range(n):
#     if i == f[i]:
#         ans += 1
# print(ans - 1)
#


"""
        有一个初始包含 N 个顶点、无边的无向图，顶点编号为 1 到 N，初始所有顶点均为白色，需处理 Q 条查询，
    查询分为三种类型：类型 1 为添加一条连接顶点 u 和 v 的无向边；类型 2 为将顶点 v 的颜色翻转（白色变黑色、黑色变白色）；
    类型 3 为判断能否从顶点 v 出发经过零条或多条边到达一个黑色顶点，能则输出 Yes，不能则输出 No。


"""
import sys
input = sys.stdin.readline
n ,q = map(int, input().split())
d = [i for i in range(n + 1)]
black_bit = [0] * (n + 1)
color = [False] * (n + 1)
def find(x):
    if x != d[x]:
        d[x] = find(d[x])
    return d[x]

def research(u, v):
    a = find(u)
    b = find(v)
    if a != b:
        d[b] = a
        black_bit[a] += black_bit[b]

for _ in range(q):
    cur = list(map(int, input().split()))
    if cur[0] == 1:
        research(cur[1], cur[2])
    elif cur[0] == 2:
        root = find(cur[1])
        if color[cur[1]]:
            black_bit[root] -= 1
        else:
            black_bit[root] += 1
        color[cur[1]] = not color[cur[1]]
    else:
        if black_bit[find(cur[1])]:
            print("Yes")
        else:
            print('No')