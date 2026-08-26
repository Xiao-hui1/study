# n = int(input())
# l = len(str(n))
# import math
# even = l // 2
# first = n // (10 ** (l-1))
# def fun(a):
#     d = str(a)
#     size = len(d)
#     odd = ['1','3','5','7','9']
#     for i in range(size):
#         if i % 2 == 0 and d[size - i - 1] not in odd:
#             return 0
#         elif i % 2 and d[size - i - 1] in odd:
#             return 0
#     return 1
# count = 0
# for i in range(1, n + 1):
#     if i % 2:
#         if fun(i):
#             count += 1
# print(count)

# v = input().split()
# n = int(v[0])
# d = v[1]
# s = []
# po = d.find('.')
# t = int(d[:po])
# d = int(d[po + 1:])
# while t:
#     s.append(t % 2)
#     t //= 2
#
# s = s[::-1]
# pre = len(s)
#
# size = len(s)
#
# if pre + n >= size:
#     s = s + [0] * (pre + n - size)
#     sum = 0
#     for i in range(pre + n):
#         sum += s[pre + n - 1 - i] * (1 << i)
#     print(sum)
# else:
#     sum = 0
#     for i in range(pre + n):
#         sum += s[pre + n - 1 - i] * (1 << i)
#     if s[pre + n]:
#         print(sum + 1)
#     else:
#         print(sum)

# import math
# r = math.sqrt(233 * 233 + 666 * 666)
# res = r + math.asin(666 / r) * r
# print(round(res))


# n = int(input())
# d = list(map(int, input().split()))
# count = n
# for i in d:
#     if i == 1:
#         count -= 1
# print(count)

# def fun(a, b):
#     return (a + b) // 2
# n = int(input())
# res = []
# for i in range(n):
#     a,b,c,k = map(int, input().split())
#     for i in range(k):
#         a, b, c = fun(c, b), fun(a, c), fun(a,b)
#         if a == b and b == c:
#             break
#     res.append((a, b, c))
# for (a, b, c) in res:
#     print(a, b, c)

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# a.sort()
# ans = float('inf')
#
# for i in range(n - m + 1):
#     j = i + m - 1
#     begin_val = a[i] * a[i]
#     end_val = a[j] * a[j]
#     ans = min(ans, end_val - begin_val)
#
# print(ans)


import sys


def solve():
    a = input().strip()
    b = input().strip()

    ans = 0
    lst = -1
    state = -1

    for i in range(len(a)):
        if a[i] == '.' and b[i] == '.':
            continue

        if lst != -1:
            ans += i - lst - 1

        if a[i] == '#' and b[i] == '#':
            state = 3
        elif a[i] == '#' and b[i] == '.':
            if state == 2:
                ans += 1
                state = 3
            else:
                state = 1
        elif a[i] == '.' and b[i] == '#':
            if state == 1:
                ans += 1
                state = 3
            else:
                state = 2

        lst = i

    print(ans)
if __name__ == "__main__":
    _ = 1
    while _ > 0:
        solve()
        _ -= 1