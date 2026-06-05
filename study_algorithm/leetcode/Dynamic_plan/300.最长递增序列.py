"""
        获取当前的最长严格递增序列的方法是:
            从开始位置找到当前位置的前一个位置,如果前面的值小于当前的值的话代表前面的是它的递增序列部分,判断 这部分的递增序列 + 1是否大于当前记录的最大序列,
            如果大于则更改为当前此序列长度

"""

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


#上述代码只可以用于数据较小的题目当中，如果数据较大则需要使用二分 + 贪心的思想：
n = int(input())
nums = list(map(int, input().split()))

f = [0] * n
len = 0
for i in range(n):
    if len == 0 or nums[i] > nums[len]:
        len += 1
        f[len] = nums[i]
    else:
        r = i
        l = 0
        while l < r:   #利用二分查找，最小且大于等于当前数的位置
            mid = (l + r) // 2
            if nums[mid] >= nums[i]:
                r = mid
            else:
                l = mid + 1
        f[l] = nums[i]  #把当前的数插入到大于自己的最小数的位置，更新最小的位置
print(len)

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))