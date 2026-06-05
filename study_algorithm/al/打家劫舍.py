from algorithm_python.test import Solution

class Solution:
    def reRob(self, nums: list[int], left: int, right: int) -> int:
        if left > right:
            return

        dp = [0] * len(nums)

        dp[left] = nums[left]
        dp[left + 1] = max(nums[left], nums[left + 1])

        for i in range(2, right + 1, 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[right]


    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        one = self.reRob(nums, 1, len(nums) - 1)
        two = self.reRob(nums, 0, len(nums) - 2)

        return max(one, two)


# #myself:
# class Solution:
#     def rob(self, nums: list[int]) -> int:
#         dp1 = []
#         dp2 = []
#         size = len(nums) - 1
#         if not size:
#             return nums[0]
#         for i in range(len(nums)):
#             if i == 0:
#                 dp1.append(nums[i])
#             elif i == 1:
#                 dp1.append(max(nums[0], nums[1]))
#                 dp2.append(nums[i])
#             elif i == 2:
#                 dp2.append(max(nums[2], nums[1]))
#
#             if 1 < i < size:
#                 dp1.append(max(dp1[i - 1], dp1[i - 2] + nums[i]))
#             if 2 < i:
#                 dp2.append(max(dp2[i - 2], dp2[i - 3] + nums[i]))
#
#         return max(dp1[len(dp1) - 1], dp2[len(dp2) - 1])

if "__name__"=='__main__':
    s = Solution()
    print(s.rob([1,5,8,6,8,2,4,54]))