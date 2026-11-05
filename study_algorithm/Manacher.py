"""
Manacher 算法 —— O(n) 求最长回文子串

核心思想：在字符间插入分隔符（如 '#'），把所有回文统一成奇数长度，
利用已求出的回文半径的对称性跳过重复计算。

p[i] 表示变换后字符串以 i 为中心的回文半径（含中心，# 也算）。
对应原串：以原串位置为中心的最长回文长度 = p[i] - 1。
"""


def manacher(s):
    """返回 (最长回文长度, 最长回文子串)；空串返回 (0, '')"""
    if not s:
        return 0, ""

    t = "#" + "#".join(s) + "#"   # 变换后的串，长度 2n+1
    n = len(t)
    p = [0] * n                    # 回文半径数组
    c = r = 0                      # c: 当前最右回文中心, r: 其右边界（不含）

    for i in range(n):
        if i < r:
            # i 关于 c 的对称点为 2c-i，利用其半径加速（不能越过右边界）
            p[i] = min(r - i, p[2 * c - i])
        # 中心扩展
        while i - p[i] >= 0 and i + p[i] < n and t[i - p[i]] == t[i + p[i]]:
            p[i] += 1
        # 更新最右回文
        if i + p[i] > r:
            c, r = i, i + p[i]

    # 找最大半径，还原到原串
    # p[i] - 1 即臂长 = 原串中以该中心扩展出的最长回文长度
    center = max(range(n), key=lambda i: p[i])
    length = p[center] - 1                       # 原串中的回文长度
    start = (center - p[center] + 1) // 2        # 原串中的起始下标
    return length, s[start:start + length]


def count_palindromes(s):
    """（附加）统计回文子串总数，同样基于 Manacher"""
    if not s:
        return 0
    t = "#" + "#".join(s) + "#"
    p = [0] * len(t)
    c = r = 0
    for i in range(len(t)):
        if i < r:
            p[i] = min(r - i, p[2 * c - i])
        while i - p[i] >= 0 and i + p[i] < len(t) and t[i - p[i]] == t[i + p[i]]:
            p[i] += 1
        if i + p[i] > r:
            c, r = i, i + p[i]
    # 每个中心贡献 p[i] // 2 个回文
    return sum(x // 2 for x in p)


if __name__ == "__main__":
    print(manacher("babad"))     # (3, 'bab') 或 'aba'
    print(manacher("cbbd"))      # (2, 'bb')
    print(manacher("a"))         # (1, 'a')
    print(manacher("forgeeksskeegfor"))  # (10, 'geeksskeeg')
    print(count_palindromes("aaa"))      # 6: a,a,a,aa,aa,aaa
