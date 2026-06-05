import sys, os
"""
        平衡树：
            平衡树分为很多种，例如：平衡二叉树，树堆，伸展树，SBT树，红黑树等
            1.平衡二叉树：
"""
class Node(object):
    def __init__(self, x):
        self.val = x
        self.right= None
        self.left = None
        self.height = 1

def updateHeight(node):
    pass

def LL_Rotation(node):
    temp = node.left
    node.left = temp.right
    temp.right = node
    updateHeight(node)
    updateHeight(temp)
    return temp

def RR_Rotation(node):
    temp = node.right
    node.right = temp.left
    temp.left = node
    updateHeight(node)
    updateHeight(temp)
    return temp


def LR_Rotation(node):
    node.left = RR_Rotation(node.left)
    return LL_Rotation(node)


def RL_Rotation(node):
    node.right = RR_Rotation(node.right)
    return RR_Rotation(node)


def Height(node):
    return 1


def Insert(node, val):
    if not node:
        node = Node()
        node.left = node.right = None
        node.val = val
        return node
    if node.val == val:
        return node
    if val < node.val:  #插入左子树
        node.left = Insert(node.left, val)   #注意插入后将结果挂接到node.left
        if (Height(node.left) - Height(node.right) == 2):
            #插入后看是否平衡，若平衡，则沿高度大的路径判断
            if val < node.left.val: #判断是LL型还是LR型，即是left的left还是right
                node = LL_Rotation(node)
            else:
                node = LR_Rotation(node)
    else:       #插入右子树
        node.right = Insert(node.right, val)
        if (Height(node.right) - Height(node.left) == 2):
            if val < node.right.val:
                node = RR_Rotation(node)
            else:
                node = RL_Rotation(node)
    updateHeight(node)
    return node

def create(node):
    num = int(input())
    for i in range(num):
        x = int(input())
        node = Insert(node, x)
    return node



#------------------------------------------------------------------------



class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # 叶子初始高度1，方便计算


class AVLTree:
    # 获取节点高度
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # 获取平衡因子
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # 右旋
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    # 左旋
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # 插入
    def insert(self, node, val):
        # 1. BST 插入
        if not node:
            return AVLNode(val)
        elif val < node.val:
            node.left = self.insert(node.left, val)
        elif val > node.val:
            node.right = self.insert(node.right, val)
        else:
            return node  # 不允许重复

        # 2. 更新高度
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # 3. 计算平衡因子
        balance = self.get_balance(node)

        # 4. 4种失衡

        # LL
        if balance > 1 and val < node.left.val:
            return self.right_rotate(node)

        # RR
        if balance < -1 and val > node.right.val:
            return self.left_rotate(node)

        # LR
        if balance > 1 and val > node.left.val:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # RL
        if balance < -1 and val < node.right.val:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    # 找最小值
    def min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # 删除
    def delete(self, node, val):
        # 1. BST 删除
        if not node:
            return node

        elif val < node.val:
            node.left = self.delete(node.left, val)

        elif val > node.val:
            node.right = self.delete(node.right, val)

        else:
            # 只有一个孩子 or 无孩子
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # 两个孩子：找后继
            temp = self.min_node(node.right)
            node.val = temp.val
            node.right = self.delete(node.right, temp.val)

        if node is None:
            return node

        # 2. 更新高度
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # 3. 平衡因子
        balance = self.get_balance(node)

        # LL
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        # LR
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # RR
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        # RL
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    # 中序遍历（一定有序）
    def inorder(self, node):
        res = []
        if node:
            res += self.inorder(node.left)
            res.append(node.val)
            res += self.inorder(node.right)
        return res