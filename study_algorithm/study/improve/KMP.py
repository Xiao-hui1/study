import sys, os
"""
        KMP算法：
            先给模式串建一个 next 数组，记录每一位不匹配时该跳去哪里。
            匹配时主串不回退，只动模式串。
            模式串按 next 数组跳，避免重复比较，实现最快匹配。

"""

# s = input()
# sub = input()
# size = len(s)
# l = len(sub)
# next = [0 for _ in range(l + 1)]
#
# def get_next(t):
#     j = 0
#     k = -1
#     next[0] = -1
#     while j<l:
#         if k == -1 or t[j] == t[k]:
#             next[j + 1] = k + 1         #K 代表当前前缀和后缀有多个个是匹配的了
#             j += 1
#             k += 1
#         else:
#             k = next[k]
#
# def kmp(s, sub):
#     i = j = 0
#     get_next(sub)
#     while i < size:
#         if s[i] == sub[j] or j == -1:
#             i += 1
#             j += 1
#         else:
#             j = next[j]
#
#         if j == l:
#             print(i - j + 1)
#             j = next[j]
#
# kmp(s, sub)
# print(*next[1:])


def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    lps = build_lps(pattern)
    i = 0
    j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def solve(A, B):
    n = len(A)
    if sorted(A) != sorted(B):
        return -1
    if n == 0:
        return 0
    doubled_A = A + A
    pos = kmp_search(doubled_A, B)
    if pos == -1:
        return -1
    return pos

T = int(input())
for _ in range(T):
    A = input().strip()
    B = input().strip()
    result = solve(A, B)
    print(result)