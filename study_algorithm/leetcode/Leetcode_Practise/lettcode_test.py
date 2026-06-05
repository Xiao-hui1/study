class Solution1:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        size = len(nums)
        if size <=3:
            if size<3:
                return [[]]
            else:
                if sum(nums) == 0:
                    return [nums]
        #nums.sort
        val = []
        for i in range(size):
            for j in range(size-1,i+1,-1):
                # if nums[i] + nums[j] > nums[j]:
                #     continue
                if (-1*(nums[i] + nums[j])) in nums[i+1:j-1]:
                    # print(nums[i+1:j-1])
                    # print((-1*(nums[i] + nums[j])))
                    # print(i,j)
                    if [nums[i],nums[j],(-1*(nums[i] + nums[j]))] not in val:
                        val.append([nums[i],nums[j],(-1*(nums[i] + nums[j]))])
        return val


class Solution2:
    #数学函数的测试
    def fun(self):
        #判断一个数字是不是完全数
        import math
        num = int(input())
        if int(math.sqrt(num)*math.sqrt(num)) == num:
            print("Yes!")
        else:
            print("No")
        #   math.pow(num,2) == num ** 2     两个表达式的值相等
        #   字符串的大小写转换
        st = input("")
        st.strip()
        st.upper()  #转换成大写字母
        st.lower()  #转换成小字母
        #内联函数的使用方法
        return lambda x : x**2



# class Solution3:
#     def getRow(self, rowIndex: int) -> list[int]:
#         dp = [0]*rowIndex
#         def hui(x, y):
#             if y == 0 or x == y:
#                 return 1
#             return hui(x-1,y-1) + hui(x-1,y)
#
#         for i in range(rowIndex):
#             dp[i] = hui(rowIndex - 1, i)
#         return dp
# s = Solution()
# print(s.getRow(3))


class Solution4:
    def isSubsequence(self, s: str, t: str) -> bool:
        s =list(s)
        t = list(t)
        if len(s) > len(t):
            return  False
        elif len(s) == len(t) and s != t:
            return False
        elif not len(s):
            return True
        cur = 0
        per = t.index(s[0])-1
        t.pop(per+1)
        for i in s[1:]:
            if i in t[per+1:]:
                cur = t.index(i)
                if cur < per:
                    print(cur,per)
                    return False
                t.pop(cur)
                print(t)
                per = cur-1
            else:
                print('2')
                return False
        return True



"""
    最长回文串的动态规划解法思想：
    1.循环遍历字符串
    2.确认下标i,j的值是否相同。
    3.确定中间串（i+1 - j-1）是否是回文串，如果中间不是那么此字符串一定不是回文串
    4.然后再扩散，并且记录最长的子串长度
        a   b   a   b   a   a   b
        
        0   1   2   3   4   5   6               当只有一个字符串的时候一定是一个回文串，所以直接设置为true
    0   1   0   1   0   1   0   0
    1       1   0   1   0   0   0
    2           1   0   1   0   0
    3               1   0   0   1
    4                   1   1   0
    5                       1   0
    6                           1
"""


class Solution5:
    def isSubsequence(self, s: str, t: str) -> bool:
        print('最长回文串的动态规划解法思想:')
        def longestPalindrome(self, s: str) -> str:
            size = len(s)
            if size < 2:
                return s
            dp = [[0] * size for _ in range(size)]
            max_len = 1
            begin = 0

            for i in range(size):
                dp[i][i] = 1

            for j in range(2, size + 1):

                for i in range(size):
                    l = j + i - 1

                    if l >= size:
                        break

                    if s[i] != s[l]:
                        dp[i][l] = 0
                    else:
                        if l - i < 3:
                            dp[i][l] = 1
                        else:
                            dp[i][l] = dp[i + 1][l - 1]

                        if dp[i][l] and l - i + 1 > max_len:
                            max_len = l - i + 1
                            begin = i
            return s[begin:begin + max_len] #利用切片返回回文串



if __name__ == '__main__':
    # s = Solution4()
    # print(s.isSubsequence("leetcode",'dfdsdfjsdjfjeljkfghgjdjfkssjff'))
    #
    # s = Solution1()
    # print(s.threeSum([1,2,-2,-1]))
    # st = Solution2()
    # st.fun()


    nums = [5,7,7,8,8,10]
    target = 8
    front = back = 0
    fountf = bcount = 0
    left, right = 0, len(nums) - 1

    # 判断是否为空列表
    if not right:
        print([-1, -1])
    """
        使用双指针遍历列表
        如果从头和结尾双向搜索都没有找到目标值，则代表该值在列表中不存在
    """
    while left <= right:
        # 找开始下标
        if not front and nums[left] != target:
            left = left + 1
        elif nums[left] == target:
            front = 1
            fountf = left

        if not back and nums[right] == target:
            bcount = right
            back = 1
        elif nums[right] != target:
             right -= 1

        # 减少工作量，全找到了则立刻结束
        if back and front:
            break

    if front and back:
        print([fountf, bcount])
    elif front or back:
        print([max(fountf, bcount)] * 2)
    else:
        print([-1, -1])