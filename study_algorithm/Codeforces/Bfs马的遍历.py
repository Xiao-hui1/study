import collections

n, m, x, y = list(map(int, input().split()))
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

val = [[-1] * m for _ in range(n)]


dp = collections.deque([x,y])
val[x-1][y-1] = 0

while dp:
    i, j = dp.popleft() - 1, dp.popleft() - 1
    for k in range(8):
        x = i + dx[k]
        y = j + dy[k]
        if 0 > x or x >= n or 0 > y or y >= m or val[x][y] != -1:
            continue
        val[x][y] = val[i][j] + 1
        dp.extend([x + 1, y + 1])

for i in range(n):
    print(*val[i])


"""
    有一个 H 行 W 列的网格，用 (i,j) 表示位于第 i 行（从上往下数）第 j 列（从左往右数）的格子，
    每个格子的状态用字符 A_i,j 表示，含义如下：
        . ：空格子。
        # ：障碍格子。
        S ：起点格子。
        G ：终点格子。
        o ：开着的门格子。
        x ：关着的门格子。
        ? ：开关格子。
    高桥君可以从当前格子移动到上下左右相邻的格子，但不能移动到障碍格子或关着的门格子，每次移动算一次操作。
    
    而且，每当他走到一个开关格子时，所有开着的门都会变成关着的门，所有关着的门都会变成开着的门。
    
    请判断他是否能从起点出发，最终到达终点；如果能，求出最少需要多少次操作。

"""

from collections import deque
import sys,math

input = sys.stdin.readline

h, w = map(int, input().split())
g = [input().strip() for _ in range(h)]

sx = sy = gx = gy = 0
for i in range(h):
    for j in range(w):
        if g[i][j] == 'S': sx, sy = i, j
        if g[i][j] == 'G': gx, gy = i, j

d0 = [[math.inf] * w for _ in range(h)]
d1 = [[math.inf] * w for _ in range(h)]
d0[sx][sy] = 0
q = deque([(sx, sy, 0)])
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
f = 0
while q:
    x, y, s = q.popleft()
    if x == gx and y == gy:
        print(min(d0[x][y], d1[x][y]))
        f = 1
        break
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and g[nx][ny] != '#':
            c, ns = g[nx][ny], s
            ok = 0
            if c in 'SG.':
                ok = 1
            elif c == 'o':
                ok = s == 0
            elif c == 'x':
                ok = s == 1
            elif c == '?':
                ok = 1; ns ^= 1

            cur = d0[x][y] if s == 0 else d1[x][y]
            nxt = d0[nx][ny] if ns == 0 else d1[nx][ny]
            if ok and cur + 1 < nxt:
                if ns == 0:
                    d0[nx][ny] = cur + 1
                else:
                    d1[nx][ny] = cur + 1
                q.append((nx, ny, ns))
if not f:
    print(-1)