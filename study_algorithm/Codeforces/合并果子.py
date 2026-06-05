n = int(input())

val = list(map(int, input().split()))

total = 0

import heapq
heapq.heapify(val)
while len(val) >= 2:
    cur =  heapq.heappop(val) + heapq.heappop(val)
    total += cur
    heapq.heappush(val, cur)
print(total)