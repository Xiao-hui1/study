import heapq as hp

nums = [3, 1, 4, 1, 5]
hp.heapify(nums)  # nums 变成堆：[1, 1, 4, 3, 5]

hp.heappush(nums, 0)  # 加入 0
print(hp.heappop(nums))  # 输出 0（最小值）