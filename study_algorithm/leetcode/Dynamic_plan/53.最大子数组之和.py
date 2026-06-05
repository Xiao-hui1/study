class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        pos = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                pos = i
                break
        ma = max(nums)
        for i in range(pos, len(nums)):
            if nums[i] > 0:
                dp = [0] * len(nums)
                for j in range(i, len(nums)):
                    dp[j] = dp[j - 1] + nums[j]
                    if dp[j] < 0:
                        break
                    if dp[j] > ma:
                        ma = dp[j]
        return ma



"""
        上面的代码可行但是会超时时间复杂度为O(n*m),空间复杂度为O(n)
        
        下面为可行代码,时间复杂度和空间复杂度都为O(n)
            思想为:
                从头开始进行累加,只要前面的数大于零加上就和是此段连续数组增大,
                如果小于零加上没有任何意义并且会使当前这段的变小,所以当前面面的和小于零时,当前的值就为自己的值.
"""

class Solution2:
    def maxSubArray(self, nums: list[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i - 1] >= 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)
if __name__ == '__main__':
    s = Solution2()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))