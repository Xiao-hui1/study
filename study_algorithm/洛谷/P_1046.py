data = list(map(int, input().split()))

n = int(input()) + 30

res = list(filter(lambda x: x <= n, data))

print(len(res))