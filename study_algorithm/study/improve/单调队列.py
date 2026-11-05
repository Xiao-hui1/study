"""
单调队列
    用于求一个区间内的最大或这最小值

下面案例为求求当前位置的前三个位置中的最大值和最小值

"""

# from collections import deque
# import sys


# def solve():
#     data = sys.stdin.buffer.read().split()
#     n = int(data[0])
#     k = int(data[1])
#     val = [int(x) for x in data[2 : 2 + n]]

#     q_min = deque()
#     q_max = deque()
#     ans_min = []
#     ans_max = []

#     for i in range(n):
#         # 维护最小值队列：单调递增
#         while q_min and val[q_min[-1]] >= val[i]:
#             q_min.pop()
#         q_min.append(i)

#         # 维护最大值队列：单调递减
#         while q_max and val[q_max[-1]] <= val[i]:
#             q_max.pop()
#         q_max.append(i)

#         # 删除超出窗口的队头
#         if q_min[0] <= i - k:
#             q_min.popleft()
#         if q_max[0] <= i - k:
#             q_max.popleft()

#         # 窗口形成后再记录答案
#         if i >= k - 1:
#             ans_min.append(str(val[q_min[0]]))
#             ans_max.append(str(val[q_max[0]]))

#     print(" ".join(ans_min))
#     print(" ".join(ans_max))


# solve()

from collections import deque
import sys


it = iter(sys.stdin.buffer.read().split())


def solve():
    ans = float("-inf")
    n, m = int(next(it)), int(next(it))
    d = list(map(int, (next(it) for _ in range(n))))

    pre = [0] * (n + 1)
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + d[i - 1]

    q = deque([0])
    for i in range(1, n + 1):
        while q and q[0] + m < i:
            q.popleft()
        ans = max(ans, pre[i] - pre[q[0]])
        while q and pre[q[-1]] >= pre[i]:
            q.pop()
        q.append(i)

    print(ans)


if __name__ == "__main__":
    solve()
