"""
    单调队列
        用于求一个区间内的最大或这最小值

    下面案例为求求当前位置的前三个位置中的最大值和最小值

"""

n, k = list(map(int, input().split()))

val = list(map(int, input().split()))


import collections
dp  = collections.deque()

for i in range(1, n+1):
    while dp and val[dp[-1]-1] >= val[i-1]:
        dp.pop()
    dp.append(i)
    if i - dp[0] + 1 > k:
        dp.popleft()
    if i >= k:
        print(val[dp[0]-1], end = " ")
dp.clear()

print()

for i in range(1, n+1):
    while dp and val[dp[-1]-1] <= val[i-1]:
        dp.pop()
    dp.append(i)
    if i - dp[0] + 1 > k:
        dp.popleft()
    if i >= k:
        print(val[dp[0]-1], end = " ")
dp.clear()