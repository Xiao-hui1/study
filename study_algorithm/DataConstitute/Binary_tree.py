"""
    生成二叉树
        1. 生成无序树
        2. 生成有序树
    查找二叉树节点
        1.使用深度优先算法查找结点
            深度优先查找分为：
                a.根左右
                b.左根右
                c.左右根
        2.使用广度优先算法查找节点
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.ltree = None
        self.rtree = None

class BinaryTree:
    def __init__(self,data = None):
        self.root = None
        self.data = data

    def add(self, value):
        queue = []  #使用队列来实现广度优先
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        queue.append(self.root)
        #通过循环查找空缺的节点位置
        while True:
            node = queue.pop(0)
            if node.ltree is None:
                node.ltree = new_node
                return
            else:
                queue.append(node.ltree)

            if node.rtree is None:
                node.rtree = new_node
                return
            else:
                queue.append(node.rtree)

    #创建二叉搜索树
    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        else:
            current = self.root
            parent = None
        while True:
            parent = current
            if value < parent.data:
                current = parent.ltree
                if current is None:
                    parent.ltree = node
                    return
            else:
                current = parent.rtree
                if current is None:
                    parent.rtree = node
                    return
    #查找指定节点的位置与其双亲节点的位置
    def get_node_with_parent(self, value):
        parent = None
        current = self.root
        if current is None:
            return (current, parent)
        while True:
            if value == current.data:
                return (current, parent)
            elif value < current.data:
                parent = current
                current = current.ltree
            else:
                parent = current
                current = current.rtree


    #进行节点的删除操作
    def remove(self, value):
        parent, node = self.get_node_with_parent(value)
        if parent is None and node is None:
            return False
        children = 0
        if node.ltree is None and node.rtree is None:
            children = 0
        elif node.ltree and node.rtree:
            children = 2
        else:
            children = 1
        if children == 0:
            if parent:
                if parent.rtree is node:
                    parent.rtree = None
                else:
                    parent.ltree = None
            else:
                self.root = None
        elif children == 1:
            next_node = None
            if node.ltree:
                next_node = node.ltree
            else:
                next_node = node.rtree
            if parent:
                if parent.ltree is node:
                    parent.ltree = next_node
                else:
                    parent.rtree = next_node
            else:
                self.root = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.rtree
            while leftmost_node.ltree:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.ltree
            node.data = leftmost_node.data
            if parent_of_leftmost_node.ltree == leftmost_node:
                parent_of_leftmost_node.ltree = leftmost_node.rtree
            else:
                parent_of_leftmost_node.rtree = leftmost_node.rtree

    def breadth_travel(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            #取出队首的节点，并输出
            node = queue.pop(0)
            print(node.data,end=' ')

            #判断左右子树是否为空
            if node.ltree is not None:
                queue.append(node.ltree)
            if node.rtree is not None:
                queue.append(node.rtree)

    def preorder_travel(self,root):
        #根左右的形式遍历
        if root is not None:
            print(root.data, end=' ')
            self.preorder_travel(root.ltree)
            self.preorder_travel(root.rtree)

    def inorder_travel(self,root):
        #左根右的形式遍历
        if root is not None:
            self.inorder_travel(root.ltree)
            print(root.data, end=' ')
            self.inorder_travel(root.rtree)

    def inorder(self,root):
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

    def postorder_travel(self,root):
        #以左右根的形式遍历
        if root is not None:
            self.postorder_travel(root.ltree)
            self.postorder_travel(root.rtree)
            print(root.data, end=' ')

    #实现深度优先二叉树的建立
    def sort_tree(self,root):
        if root is not None:
            self.sort_tree(root.ltree)
            root.ltree.data = self.data.pop(0)
            self.sort_tree(root.rtree)
#----------------------------------------------------------------------------------------------------

"""二叉树的生成"""
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Node:
        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2

            root = Node(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)

if __name__ == '__main__':
    # li = list(input().split())
    # tree = BinaryTree(li)
    # for i in li:
    #     tree.add(i)
    # tree.sort_tree(tree.root)
    # tree.breadth_travel()
    # print()
    # tree.preorder_travel(tree.root)
    # print()
    # tree.inorder_travel(tree.root)
    # print()
    # tree.postorder_travel(tree.root)


    # s = BinaryTree([1,2,3,4,5])
    # s.insert(1)
    # s.insert(4)
    # s.insert(5)
    # s.insert(3)
    # s.postorder_travel(s.root)
    num = int(input())
    val = []
    res = [0] * num
    for i in range(num):
        val.append(list(map(int, input().split())))

    for idx, row in enumerate(val):
        while row[0] != row[1]:
            if row[0] > row[1]:
                res[idx] += row[3]
                print(row[3])
                row[0] += -1
            else:
                if row[4] <= (row[0]*2 -row[0]) * row[2] and row[0]*2 <= row[1] or(row[0]*2 > row[1] and (row[0]*2-row[1])*row[2]+row[4] < (row[1] - row[0]) * row[2]) :
                    res[idx] += row[4]
                    print('+',row[4])
                    row[0] *= 2
                else:
                    res[idx] += row[2]
                    print('+',row[2])
                    row[0] += 1
    for i in res:
        print(i)