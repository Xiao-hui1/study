import sys


it = iter(sys.stdin.buffer.read().split())


def z_func(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(z[i - l], r - i + 1)
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z


def solve():
    n, m, k = map(int, (next(it) for _ in range(3)))
    a, b = next(it).decode(), next(it).decode()

    z = z_func(b + "#" + a)

    cnt = [0] * (m + 2)
    for i in range(m + 1, n + 1 + m):
        cnt[min(z[i], m)] += 1

    for i in range(m - 1, -1, -1):
        cnt[i] += cnt[i + 1]

    for i in range(k):
        cur = int(next(it))
        if cur > m:
            print(0)
        else:
            print(cnt[cur] - cnt[cur + 1])


if __name__ == "__main__":
    solve()
