"""
    求最小路径和:
        使用动态规划的策略,从后面往前面走,先确定后面到最右下角位置的最短路径,最后得到从最左上角到右下角的最短路径和
"""

def minPathSum(grid: list[list[int]]) -> int:
    dp = [[0] * len(grid[0]) for _ in range(len(grid))]
    row = len(grid) - 1
    col = len(grid[0]) - 1
    dp[-1][-1] = grid[-1][-1]
    for i in range(row - 1, -1, -1):
        dp[i][col] += dp[i + 1][col] + grid[i][col]
    for i in range(col - 1, -1, -1):
        dp[row][i] = dp[row][i + 1] + grid[row][i]
    print(dp)
    for i in range(row - 1, -1, -1):
        for j in range(col - 1, -1, -1):
            dp[i][j] = min(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]
    for i in dp:
        print(i)
    return dp[0][0]

if __name__ == '__main__':
    s = [[1,3,1],[1,5,1],[4,2,1]]
    x = minPathSum(s)
    print(x)
