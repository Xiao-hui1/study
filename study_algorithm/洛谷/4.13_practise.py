# a, b, c = map(int, input().split())
# import collections, sys
# d = collections.Counter([a,b,c])
# for i in d.values():
#     if i >= 2:
#         print('Yes')
#         exit(0)
# print('No')


# n ,m, k = map(int, input().split())
# d = [0] * n
# res = []
# for _ in range(k):
#     a, b = map(int, input().split())
#     d[a - 1] += 1
#     if d[a - 1] == m:
#         res.append(a)
# print(*res)


n = int(input())
state = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    x, y = map(int, input().split())
    if (x == 0 and y == 0) or state[x] or state[y]:
        state[i] = 1
print(sum(state))