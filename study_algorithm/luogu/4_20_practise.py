# # n, m, c = map(int, input().split())
# # d = list(map(int, input().split()))
# # import collections
# # sta = collections.Counter(d)
# # val = []
# # for i in sta.keys():
# #     val.append((i,sta[i]))
# # val.sort()
# # res = []
#
#
#
# # n , m = map(int, input().split())
# # d = []
# # for i in range(n):
# #     d.append(input().strip())
# # num = [[1] * n for _ in range(n)]
# # for i in range(n):
# #     for j in range(n):
# #         if d[i][j] == '#':
# #             num[i][j] = 2
# # import collections
# # d = []
# # for i in range(n - m + 1):
# #     for j in range(m - 1, n):
# #         t = ''
# #         for x in range(m):
# #             for y in range(m):
# #                 t = t + str(num[i + x][j + y - m + 1])
# #         d.append(t)
# # d = collections.Counter(d)
#
#
# # import bisect
# # n = int(input())
# # d = list(map(int, input().split()))
# # ans = [0,d[0]]
# # val = [d[0],d[0]]
# # s = 2 * d[0]
# # print(s)
# # cur = 2
# # for i in range(1, n):
# #     pos = bisect.bisect_right(ans, d[i])
# #     if pos == cur:
# #         s -= val[-1]
# #         ans.append(d[i])
# #         val[-1] = min(val[-1], abs(ans[-2] - d[i]))
# #         val.append(abs(d[i] - ans[-2]))
# #         s += val[-1] + val[-2]
# #     else:
# #         s -= val[pos - 1] + val[pos]
# #         ans.insert(pos, d[i])
# #         val[pos - 1] = min(val[pos - 1],abs(ans[pos - 1] - d[i]))
# #         val[pos] = min(val[pos], abs(ans[pos + 1] - d[i]))
# #         val.insert(pos, min(abs(ans[pos - 1] - d[i]), abs(ans[pos + 1] - d[i])))
# #         s += val[pos - 1] + val[pos] + val[pos + 1]
# #     cur += 1
# #     print(s)
#
#
# import bisect
# n = int(input())
#
# inputs = []
# while len(inputs) < n:
#     inputs.extend(list(map(int, input().split())))
# positions = [0]
#
# mp = {0: 0}
#
# INF = 10 ** 9
# d = [INF] * (n + 2)
# tot = 0
# for i in range(1, n + 1):
#     p = inputs[i - 1]
#     if i == 1:
#         d[0] = p
#         tot += p
#     pos = bisect.bisect_right(positions, p)
#
#     left_val = positions[pos - 1]
#     idl = mp[left_val]
#     tot -= d[idl]
#     d[idl] = min(d[idl], p - left_val)
#     tot += d[idl]
#     d[i] = min(d[i], p - left_val)
#
#     if pos < len(positions):
#         right_val = positions[pos]
#         idr = mp[right_val]
#
#         tot -= d[idr]
#         d[idr] = min(d[idr], right_val - p)
#         tot += d[idr]
#         d[i] = min(d[i], right_val - p)
#     tot += d[i]
#     positions.insert(pos, p)
#     mp[p] = i
#     print(tot)





t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    d = []
    f = 0
    r = 0
    for i in s:
        if i == '(':
            d.append('(')
        else:
            if not d:
                r += 1
                if r > 1:
                    print('NO')
                    f = 1
                    break
            else:
                d.pop()
    if not f:
        if (len(d) == 1 and r == 1) or (not d and not r):
            print('YES')
        else:
            print('NO')
