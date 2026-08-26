# s = input().strip()
# i = int(s[0])
# j = int(s[2])
# if j < 8:
#     print(f"{i}-{j + 1}")
# elif i == 8 and j == 8:
#     print(f"{i}-{j}")
# else:
#     print(f"{i + 1}-{1}")


# ---------------------------------


# h, w = map(int, input().split())
# d = [[0]*w for i in range(h)]
# for i in range(h):
#     s = input().strip()
#     for j in range(w):
#         if s[j] == '#':
#             d[i][j] = 1
#
# count = [[0] * w for _ in range(h)]
# flag = 1
# for i in range(h):
#     for j in range(w):
#         if d[i][j] == 1:
#             if 0 <= i - 1 < h and 0 <= j < w:
#                 count[i][j] += d[i-1][j]
#             if 0 <= i + 1 < h and 0 <= j < w:
#                 count[i][j] += d[i+1][j]
#             if 0 <= i < h and 0 <= j - 1 < w:
#                 count[i][j] += d[i][j-1]
#             if 0 <= i < h and 0 <= j + 1 < w:
#                 count[i][j] += d[i][j+1]
#             if count[i][j] not in [2,4]:
#                 flag = 0
#                 break
# if flag == 1:
#     print('Yes')
# else:
#     print('No')


# -------------------------------------------------
# t = int(input())
# d = []
# ans = []
# for i in range(t):
#     d.append(list(map(int, input().split())))
# for i in range(t):
#     m = min(d[i][0],d[i][2])
#     if m <= (d[i][1] + d[i][0] + d[i][2]) - 2 * m:
#         ans.append(m)
#     else:
#         ans.append(d[i][1] + (d[i][0] + d[i][2] - 2 * d[i][1]) // 3)
#
# for i in ans:
#     print(i)


#-----------------------------------------------------------

# n , k = map(int, input().split())
# p = 1 << n
# avg = k // p
# ans = [avg] * p
# week = p - sum(ans)
# if not week:
#     print(*ans)
# else:
#     f = 0
#     left = 0
#     right = p - 1
#     for _ in range(week):
#         if f:
#             ans[left] += 1
#             left += 2


N, K = map(int, input().split())

length = 2 ** N
num_pairs = length // 2

base_val = K // length
remainder = K % length

A = [base_val] * length

if remainder > num_pairs:
    for i in range(0, length, 2):
        A[i] += 1

    remaining_val = remainder - num_pairs
    step = num_pairs / remaining_val

    for i in range(remaining_val):
        pair_idx = int(i * step)
        A[2 * pair_idx + 1] += 1

else:
    if remainder > 0:
        step = num_pairs / remainder
        for i in range(remainder):
            pair_idx = int(i * step)
            A[2 * pair_idx] += 1

current_A = A[:]
max_imbalance = 0

for _ in range(N):
    current_max = max(current_A)
    current_min = min(current_A)
    current_range = current_max - current_min

    max_imbalance = max(max_imbalance, current_range)

    next_A = []
    for i in range(0, len(current_A), 2):
        next_A.append(current_A[i] + current_A[i + 1])

    current_A = next_A

print(max_imbalance)
for val in A:
    print(val,end = ' ')