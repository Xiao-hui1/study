# 给你一个任务数组 tasks ，其中 tasks[i] = [actuali, minimumi] ：
#
# actuali 是完成第 i 个任务 需要耗费 的实际能量。
# minimumi 是开始第 i 个任务前需要达到的最低能量。
# 比方说，如果任务为 [10, 12] 且你当前的能量为 11 ，那么你不能开始这个任务。如果你当前的能量为 13 ，你可以完成这个任务，且完成它后剩余能量为 3 。
#
# 你可以按照 任意顺序 完成任务。
#
# 请你返回完成所有任务的 最少 初始能量


class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        tasks.sort(key= lambda x: x[1] - x[0])
        val = 0
        for i , j in tasks:
            val = val + i if val + i >= j else j
        return val


if __name__ == '__main__':
    st = Solution()
    tasks = [[1,2],[3,4]]
    st.minimumEffort(tasks)