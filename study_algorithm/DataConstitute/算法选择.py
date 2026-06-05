from sort_algorithm import *
"""
    使用快速排序的思想在无序列表中查找第i个最小或者最大值
"""

def quick_select(array, start, end, k):
    split = QuickSort.partition(array, start, end)
    if split == k:
        return array[split]
    elif split < k:
        return quick_select(array, split + 1, end, k)
    else:
        return quick_select(array, start, split - 1, k)

"""
    主元选择:
        将列表中的元素五五一组，对每组的数据进行排序，然后找到每组中的中位数，在返回的中位数中找到列表的中位数，以中位数为主元进行选择
"""

class QuickSort2:
    #获得中位数（主元）
    def median_of_medians(self, array):
        sublists = [array[j:j+5] for j in range(0, len(array), 5)]
        medians = []
        for sublist in sublists:
            medians.append(sorted(sublist)[len(sublist)//2])
        if len(medians) <= 5:
            return sorted(medians)[len(medians)//2]
        else:
            return self.median_of_medians(medians)

    #获得中位数的下标
    def get_index(self, array, start, end, median):
        if start == end:
            return start
        else:
            return start + array[start:end+1].index(median)

    #交换值
    def swap(self, array, start, end):
        temp = array[start]
        array[start] = array[end]
        array[end] = temp

    def partition(self, array, start, end):
        if start == end:
            return start
        else:
            nearest_median = self.median_of_medians(array[start : end+1])
            index = self.get_index(array, start, end, nearest_median)
            self.swap(array, start, index)
            pivot = array[start]
            pivot_index = start
            less = end
            greater = start + 1
            while True:
                while greater < end and array[greater] < pivot:
                    greater += 1  # 左指针
                while less >= start and array[less] > pivot:
                    less -= 1  # 右指针
                if greater < less:
                    array[greater], array[less] = array[less], array[greater]
                else:
                    break
            #   *** 注意  ****
            # 此处为less而不是greater是因为while结束时less会到达左边而greater会到达右边，所以应该和less进行交换。
            array[pivot_index], array[less] = array[less], array[pivot_index]
            array[less] = pivot
            return less


    def determine(self, array, start, end, k):
        split = self.partition(array, start, end)
        if split == k:
            return array[split]
        elif split < k:
            return self.determine(array, split + 1, end, k)
        else:
            return self.determine(array, start, split - 1, k)


if __name__ == '__main__':
    s = QuickSort2()
    li = [12,34,5,6,87,94,7,3,67,89,90,45,23,43,74]
    target = 6
    val = s.determine(li, 0, len(li) - 1, target - 1)
    print(li,val)