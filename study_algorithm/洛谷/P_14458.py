T = int(input())

for _ in range(T):
    n = int(input())
    number = list(map(int, input().split()))
    number.sort()
    number = [0] + number
    s = [0] * (n + 1)
    res = [0] * (n + 1)

    for i in range(1, n + 1):
        s[i] = s[i - 1] + number[i]

    r = n
    l = 1
    for i in range(n, 0, -1):
        while l > 1 and number[r] >= s[r - 1] - s[l-1]:
            l -= 1
            r -= 1
        if number[r] < s[r-1] - s[l-1]:
            res[i] = s[r] - s[l-1]
        else:
            res[i] = 0
        l += 1

    for i in range(1, n+1):
        print(res[i], end=' ')
    print()