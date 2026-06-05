"""
    动态规划
"""

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        dp = [triangle[0]] + [[0] * len(triangle[i]) for i in range(1,len(triangle))]
        row = len(triangle)
        col = len(triangle[-1])
        for i in range(1,row):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        for i in range(2,row):
            for j in range(1,len(triangle[i]) - 1):
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]

        return min(dp[-1])


if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))