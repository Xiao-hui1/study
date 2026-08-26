# n = int(input())
# mi = 0
# ma = float('inf')
# for i in range(n):
#     a, b = map(int, input().split())
#     mi = max(mi, a // (b + 1) + 1)
#     ma = min(ma, a // b)
# print(mi, ma)


# k = int(input())
# da = input().split()
# s = da[0].strip()
# c1 = da[1]
# c2 = da[2]
# l = len(s)
# res = [0] * l
# count = 0
# ans = 0
# for i in range(l - 1, -1 , -1):
#     if s[i] == c2:
#         count += 1
#         res[i] = count
# for i in range(l):
#     if s[i] == c1:
#         j = i + k - 1
#         while j < l:
#             if res[j]:
#                 ans += res[j]
#                 break
#             j += 1
# print(ans)

# n = int(input())
# d = list(input().split())
# dp = [0] * 10
# for i in range(n):
#     dp[int(d[i][-1])] = max(dp[int(d[i][-1])], dp[int(d[i][0])] + 1)
# print(n - max(dp))


# t = int(input())
# for _ in range(t):
#     m, n = map(int, input().split())
#     d = []
#     for __ in range(m):
#         d.append(list(map(int, input().split())))

print("hello")