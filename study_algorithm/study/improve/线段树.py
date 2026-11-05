import sys


class SegmentTree:
    """不带懒标记：单点增加，区间求和。区间下标从 1 开始且两端均包含。"""

    def __init__(self, values):
        self.n = len(values)
        self.tree = [0] * (4 * self.n + 5)
        if self.n:
            # 根节点编号为 1；递归建立每个区间的区间和。
            self._build(1, 1, self.n, values)

    def _build(self, node, left, right, values):
        if left == right:
            # 叶节点对应原数组中的一个元素。
            self.tree[node] = values[left - 1]
            return

        middle = (left + right) // 2
        self._build(node * 2, left, middle, values)
        self._build(node * 2 + 1, middle + 1, right, values)
        # 父节点保存左右子区间之和。
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def point_add(self, index, delta):
        self._check_range(index, index)
        self._point_add(1, 1, self.n, index, delta)

    def _point_add(self, node, left, right, index, delta):
        if left == right:
            # 找到目标叶节点后更新，再沿递归路径回溯维护区间和。
            self.tree[node] += delta
            return

        middle = (left + right) // 2
        if index <= middle:
            self._point_add(node * 2, left, middle, index, delta)
        else:
            self._point_add(node * 2 + 1, middle + 1, right, index, delta)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def range_sum(self, query_left, query_right):
        self._check_range(query_left, query_right)
        return self._range_sum(1, 1, self.n, query_left, query_right)

    def _range_sum(self, node, left, right, query_left, query_right):
        if query_left <= left and right <= query_right:
            # 当前节点区间被查询区间完整覆盖，直接返回保存的区间和。
            return self.tree[node]

        middle = (left + right) // 2
        total = 0
        # 只递归访问与查询区间相交的子区间。
        if query_left <= middle:
            total += self._range_sum(node * 2, left, middle, query_left, query_right)
        if query_right > middle:
            total += self._range_sum(
                node * 2 + 1, middle + 1, right, query_left, query_right
            )
        return total

    def _check_range(self, left, right):
        if not 1 <= left <= right <= self.n:
            raise ValueError("区间必须满足 1 <= left <= right <= n")


class LazySegmentTree:
    """带懒标记：区间增加，区间求和。区间下标从 1 开始且两端均包含。"""

    def __init__(self, values):
        self.n = len(values)
        self.tree = [0] * (4 * self.n + 5)
        # lazy[node] 表示该节点区间有尚未下传给子节点的增量。
        self.lazy = [0] * (4 * self.n + 5)
        if self.n:
            self._build(1, 1, self.n, values)

    def _build(self, node, left, right, values):
        if left == right:
            self.tree[node] = values[left - 1]
            return

        middle = (left + right) // 2
        self._build(node * 2, left, middle, values)
        self._build(node * 2 + 1, middle + 1, right, values)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _apply(self, node, left, right, delta):
        # 区间每个元素增加 delta，因此区间和增加 delta * 区间长度。
        self.tree[node] += delta * (right - left + 1)
        # 先记录在当前节点，等访问子区间时再下传。
        self.lazy[node] += delta

    def _push(self, node, left, right):
        if self.lazy[node] == 0 or left == right:
            return

        # 将当前节点暂存的增量应用到两个子区间，然后清空当前标记。
        middle = (left + right) // 2
        self._apply(node * 2, left, middle, self.lazy[node])
        self._apply(node * 2 + 1, middle + 1, right, self.lazy[node])
        self.lazy[node] = 0

    def range_add(self, query_left, query_right, delta):
        self._check_range(query_left, query_right)
        self._range_add(1, 1, self.n, query_left, query_right, delta)

    def _range_add(self, node, left, right, query_left, query_right, delta):
        if query_left <= left and right <= query_right:
            # 完全覆盖时不再向下递归，使用懒标记延迟处理。
            self._apply(node, left, right, delta)
            return

        # 需要进入子区间前，先保证子节点拿到之前积累的更新。
        self._push(node, left, right)
        middle = (left + right) // 2
        if query_left <= middle:
            self._range_add(node * 2, left, middle, query_left, query_right, delta)
        if query_right > middle:
            self._range_add(
                node * 2 + 1, middle + 1, right, query_left, query_right, delta
            )
        # 子区间更新后，重新合并当前区间和。
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def range_sum(self, query_left, query_right):
        self._check_range(query_left, query_right)
        return self._range_sum(1, 1, self.n, query_left, query_right)

    def _range_sum(self, node, left, right, query_left, query_right):
        if query_left <= left and right <= query_right:
            return self.tree[node]

        # 查询需要进入子区间前先下传，确保子节点的区间和是最新的。
        self._push(node, left, right)
        middle = (left + right) // 2
        total = 0
        if query_left <= middle:
            total += self._range_sum(node * 2, left, middle, query_left, query_right)
        if query_right > middle:
            total += self._range_sum(
                node * 2 + 1, middle + 1, right, query_left, query_right
            )
        return total

    def _check_range(self, left, right):
        if not 1 <= left <= right <= self.n:
            raise ValueError("区间必须满足 1 <= left <= right <= n")


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, operation_count = data[0], data[1]
    values = data[2 : 2 + n]
    tree = SegmentTree(values)
    index = 2 + n

    for _ in range(operation_count):
        operation = data[index]
        index += 1
        if operation == 1:
            # 操作 1：单点增加，格式为 1 position delta。
            position, delta = data[index], data[index + 1]
            index += 2
            tree.point_add(position, delta)
        else:
            # 其他操作：查询区间和，格式为 operation left right。
            left, right = data[index], data[index + 1]
            index += 2
            print(tree.range_sum(left, right))


if __name__ == "__main__":
    solve()
