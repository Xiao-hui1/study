#接水问题
import heapq
n, m = list(map(int, input().split()))
li = []
val = list(map(int, input().split()))

for i in range(m):
    li.append(val[i])
heapq.heapify(li)   #创建一个大小为m的堆
for i in range(m, n):
    v = heapq.heappop(li)
    heapq.heappush(li, v + val[i])
print(max(li))