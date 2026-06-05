import sys, collections, heapq, os
"""
    线段树实现：
    
            1. 创建一个线段树，第一个节点的下标为1，当前节点的左右节点分别为：2*i 和 2*i + 1。
            2. 初始化，在每个节点中保存节点的范围[l, r]，并且记录数据，例如：最值或者[l,r]区间的和等等。（如果是带有懒标记的则还需初始化懒标记）
            3. 查询，查询[l,r]区间的最值或和，从根节点（下标为1）开始进行搜索，对当前的区间进行判断，目标区间是在当前区间的左边还是右边，
               当查询的区间覆盖当前节点表示的区间时，进行返回。
            4。 更改，对单个值进行更改可以不使用懒标记，对区间进行更改则需要使用懒标记，来节省时间，在查找更区间时对当前区间进行检查，看是否带有懒标记
                如果带有懒标记则清除当前节点的懒标记，并将懒标记向下带，返回时更新经过节点的值。
"""
class Node():
    def __init__(self, val=None, left=None, right=None, lazy=None):
        self.val = val
        self.l = left
        self.r = right
        self.lazy = lazy


n, p = map(int, input().split())
a = [0] + list(map(int, input().split()))

s = [Node(0) for _ in range(n * 4)]


# 创建线段树
def build(l, r, pos):
    s[pos].l = l
    s[pos].r = r
    if l == r:
        s[pos].val = a[l]
        return
    m = (l + r) >> 1
    build(l, m, pos << 1)
    build(m + 1, r, pos << 1 | 1)
    s[pos].val = s[pos * 2].val + s[pos * 2 + 1].val

#更新懒标记
def push_lazy(x):
    if s[x].lazy:
        s[x * 2].lazy = s[x].lazy
        s[x * 2].val += s[x].lazy * (s[x * 2].r - s[x * 2].l + 1)
        s[x * 2 + 1].lazy = s[x].lazy
        s[x * 2 + 1].val += s[x].lazy * (s[x * 2 + 1].r - s[x * 2 + 1].l + 1)
        s[x].lazy = 0

#更新区间[l,r]的值
def update(x, l, r, num):
    if s[x].l == l and s[x].r == r:
        s[x].val += num * (s[x].r - s[x].l + 1)
        s[x].lazy += num
        return
    push_lazy(x)
    mid = (s[x].l + s[x].r) >> 1
    if r <= mid:
        update(x * 2, l, r, num)
    elif l > mid:
        update(x * 2 + 1, l, mid, num)
    else:
        update(x * 2, l, mid, num)
        update(x * 2 + 1, mid + 1, r, num)
    s[x].val = s[x * 2].val + s[x * 2 + 1].val

#不使用懒标记，只可用于更新当个节点，不可用于更新区间
def up(x, i, k):
    if s[x].l == s[x].r and s[x].r == i:
        s[x].val += k
        return
    mid = (s[x].l + s[x].r) >> 1
    if i <= mid:
        up(x * 2, i, k)
    else:
        up(x * 2 + 1, i, k)
    s[x].val += k

#查询区间[l,r]的值
def query(x, l, r):
    if s[x].l == l and s[x].r == r:
        return s[x].val
    push_lazy(x)
    mid = (s[x].l + s[x].r) >> 1
    if r <= mid:
        return query(x * 2, l, r)
    elif l > mid:
        return query(x * 2 + 1, l, r)
    else:
        return query(x * 2, l, mid) + query(x * 2 + 1, mid + 1, r)


build(1, n, 1)

for i in range(p):
    da = list(map(int, input().split()))
    if da[0] == 1:
        i, k = da[1], da[2]
        up(1, i, k)
    else:
        l, r = da[1], da[2]
        print(query(1, l, r))