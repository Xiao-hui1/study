n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = 0
ma = 0
val_a = 0
val_b = 0
val_c = 0
for x in range(0, n - 2):
    val_a += a[x]
    val_b = 0
    val_c = sum(c[x + 1:])
    for y in range(x+1, n - 1):
        val_b += b[y]
        val_c -= c[y]
        dp = val_a + val_b + val_c
        if dp > ma:
            ma = dp
print(ma)