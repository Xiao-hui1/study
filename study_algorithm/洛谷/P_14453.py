# n = int(input())
# val = list(map(int, input().split()))
#
# val.sort()
# s = 0
# for i in val:
#     if s >= i:
#         s += 1
#     else:
#         s -= 1
# max = s
# val.sort(reverse=True)
# s = 0
# for i in val:
#     if s < i:
#         s -= 1
#     else:
#         s += 1
# min = s
# print(max, min)
from numpy.testing.print_coercion_tables import print_coercion_table

# def solve():
#     board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
#
#     if not board:
#         return
#
#     n = len(board)
#     m = len(board[0])
#
#     def dfs(x, y):
#         if not 0 <= x < n or not 0 <= y < m or board[x][y] != '0':
#             return
#
#         board[x][y] = 'A'
#         print(x, y)
#         dfs(x + 1, y)
#         dfs(x - 1, y)
#         dfs(x, y + 1)
#         dfs(x, y - 1)
#
#     for i in range(n):
#         dfs(i, 0)
#         dfs(i, m - 1)
#
#     for i in range(m - 1):
#         dfs(0, i)
#         dfs(n - 1, i)
#
#     for i in range(n):
#         for j in range(m):
#             if board[i][j] == 'A':
#                 board[i][j] = 'O'
#             elif board[i][j] == 'O':
#                 board[i][j] = 'X'
#
# if __name__ == '__main__':
#     solve()


t = int(input())
for _ in range(t):
    n, target = map(int, input().split())
    d = list(map(int, input().split()))
    da = [(d[i], i) for i in range(n)]
    da.sort()
    i = 0
    f = 0
    while i < n:
        cur = da[i][0]
        if cur > target:
            continue
        else:
            p = target - cur
            left = i + 1
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if da[mid][0] > p:
                    right = mid - 1
                elif da[mid][0] < p:
                    left = mid + 1
                else:
                    print(da[i][1], da[mid][1])
                    f = 1
                    break
        i += 1
        if f:
            break
