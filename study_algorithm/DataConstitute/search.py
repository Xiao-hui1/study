"""
    插值搜索
            在二分查找的基础上进行了改动，插值搜索是根据要搜索的项来确定起始位置，根据不同的搜索项可能会有不同的起始位置。
            mid = start + [(end -start)//(li[end] - li[start)*(li[pos] - li[start])]
            中间的位置为 =  起始位置 + （终止位置的下标 - 起始下标） // （最大元素 - 最小元素） * （搜索项  - 最小项））

            ***   注意//的优先级比 * 的优先级低    ***
"""

def nearest(li, start, end, search):
    #获取插值搜索的中间项
     return start + [(end - start) // (li[end] - li[start]) * (search - li[start])]

def interpolation(li, search):
    size = len(li) - 1
    start = 0
    end = size
    while start <= end:
        mid = nearest(li, start, end, search)
        if mid > end or mid < start:
            return None
        if li[mid] == search:
            return mid
        elif li[mid] > search:
            end = mid + 1
        else :
            start = mid + 1
    return None