"""
        利用动态规划进行计算:
            因为走到每一个格的方法只有两种:从上面到达/从左边到达,所以抵达每一格的结果为到达上方的路径数 加上 到达左边的路径数.


"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        dp = [[0] * len(obstacleGrid[0])  for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i]:
                break
            dp[0][i] = 1
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(1,m):
            for x in range(1,n):
                if not obstacleGrid[i][x-1] and not obstacleGrid[i-1][x]:
                    dp[i][x] = dp[i][x-1] + dp[i-1][x]
                elif not obstacleGrid[i][x-1] and obstacleGrid[i-1][x]:
                    dp[i][x] = dp[i][x-1]
                elif obstacleGrid[i][x-1] and not obstacleGrid[i-1][x]:
                    dp[i][x] = dp[i-1][x]
        for i in dp:
            print(i)
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))