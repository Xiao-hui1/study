# 由于 arr 是 [0,..,n−1] 的一个排列，若已遍历过的数中的最大值 mx 与当前遍历到的下标 i 相等，
# 说明可以进行一次分割，累加答案


class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        mx = ans = 0
        for i, v in enumerate(arr):
            mx = max(mx,v)
            if i == mx:
                ans +=1
        return ans
# 单调栈
#
# 方法一的解法有一定的局限性，若数组中存在重复元素，就无法得到正确的答案。
#
# 根据题目，我们可以发现，从左到右，每个分块都有一个最大值，并且这些分块的最大值呈单调递增。
# 我们可以用一个栈来存储这些分块的最大值。最后得到的栈的大小，也就是题目所求的最多能完成排序的块。


# class Solution:
#     def maxChunksToSorted(self, arr: List[int]) -> int:
#         stk = []
#         for v in arr:
#             if not stk or v >= stk[-1]:
#                 stk.append(v)
#             else:
#                 mx = stk.pop()
#                 while stk and stk[-1] > v:
#                     stk.pop()
#                 stk.append(mx)
#         return len(stk)



if __name__ == '__main__':
    st = Solution()
    tasks = [2,1,0,2,3,4]
    st.maxChunksToSorted(tasks)