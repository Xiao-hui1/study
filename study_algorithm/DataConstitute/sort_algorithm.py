import sys, os
from heapq import merge
from multiprocessing import heap

from pandas.core.dtypes.astype import astype_array

"""
    排序算法：
        最基本的排序算法：冒泡排序，选择排序，插入排序 。 时间复杂度为O(n^2)
        快速排序：分治类算法，把一个列表进行分区，选择一个主元，所有小于主元的元素都出现在主元的左边，大于的出现在右边。最坏情况O(n^2),平均O(n log2n)
        堆排序：。复杂度O(log2n)
"""
class QuickSort:
    def partition(self, array, start, end):
        pivot = array[start]
        pivot_index = start
        less = end
        greater = start + 1
        while True:
            while array[greater] < pivot and greater < end:
                greater += 1    #左指针
            while array[less] > pivot and less >= start:
                less -= 1   #右指针
            if greater < less:
                array[greater], array[less] = array[less], array[greater]
            else:
                break
        #   *** 注意  ****
        #此处为less而不是greater是因为while结束时less会到达左边而greater会到达右边，所以应该和less进行交换。
        array[pivot_index], array[less] = array[less], array[pivot_index]
        array[less] = pivot
        return less

    def quicksort(self, array, start, end):
        if start - end >= 0:
            return
        else:
            pivot = self.partition(array, start, end)
            self.quicksort(array, start, pivot - 1)
            self.quicksort(array, pivot + 1, end)

"""
    归并排序
"""

class MergeSort(object):

    def merge(self, left, right):
        i = j = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged


    def merge_sort(self,li):
        if len(li) <= 1:
            return li
        mid = len(li) // 2
        left = self.merge_sort(li[:mid])
        right = self.merge_sort(li[mid:])
        return merge(left, right)


from Chaptet import Heap
class Pile(Heap):

    #堆排序
    def __init__(self):
        Heap.__init__(self)

    def heap_sort(self):
        li = []
        for node in range(self.size):
            n = self.pop()
            li.append(n)
        return li



if __name__ =='__main__':
    #快速排序
    li = [12, 54, 3, 5, 6, 90, 8, 9, 10, 11, 21, 13, 14, 15]
    q = QuickSort()
    q.quicksort(li, 0, len(li) - 1)
    print(li)

    #堆排序
    h = Pile()
    li = [12, 54, 3, 5, 6, 90, 8, 9, 10, 11, 21, 13, 14, 15]
    for i in li:
        h.insert(i)
    val = h.heap_sort()
    print(val)
