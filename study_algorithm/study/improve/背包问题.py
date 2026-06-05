n, k = list(map(int, input().split()))
val = []
for _ in range(n):
    w, v = list(map(int, input().split()))
    val.append((v / w, w, v))

val.sort(key = lambda x: x[0], reverse = True)

capacity = k
total = 0

for unit, weight, value in val:
    if capacity == 0:
        break
    if weight <= capacity:
        total += value
        capacity -= weight
    else:
        total += unit * capacity
        capacity = 0
        break
print(f"{total:.2f}")