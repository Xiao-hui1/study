# n = int(input())
# s = 0
# t = -1
# for i in range(n):
#     s += t * ((i + 1) ** 3)
#     t *= -1
# print(s)


t = int(input())
d = list(map(int, input().split()))
import collections
dd = collections.Counter(d)
res = [0] * t
f = 0
for i in range(t):
    if d[i] != -1 and dd[d[i]] > 1:
        f = 1
        break
    if d[i] != -1:
        res[d[i] - 1] = 1

r = [i for i in range(1, t + 1) if res[i - 1] == 0]
ans = []
if f:
    print('No')
else:
    j = 0
    for i in range(t):
        if d[i] == -1:
            ans.append(r[j])
            j += 1
        else:
            ans.append(d[i])
    print("Yes")
    print(*ans)


# n, q = map(int, input().split())
# d = list(map(int, input().split()))
# data = d + d
# pre = [0 for i in range(2 * n + 1)]
# for i in range(1, 2 * n + 1):
#     pre[i] = pre[i - 1] + data[i - 1]
# rem = 0
# for i in range(q):
#     opr = input().split()
#     if int(opr[0]) == 1:
#         c = int(opr[1])
#         rem += c
#     else:
#         l, r = int(opr[1]), int(opr[2])
#         o = rem % n
#         print(pre[r + o] - pre[l + o - 1])