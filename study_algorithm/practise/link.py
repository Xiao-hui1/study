"""
    创建一个链表实现一下功能：
        1.isEmpty() 判断链表是否为空
        2.length()  获取链表长度
        3.find()    查找节点
        4.travel()  遍历链表
        5.add()     在头部添加节点
        6.addend()  在尾部添加节点
        7.insert(self, data, index)  在指定位置插入节点
        8.pop()     删除指定节点
        9.reverse() 逆序链表
"""
#创建链表节点
class CreatNode(object):
    #使用魔术方法会自动返回，直接使用函数的话需要自己手动设置返回。
    def __init__(self,data :int, next = None):
        self.data = data
        self.next = next

#--------------------------------------------------------------------------------
#创建完整的链表
class CreatLink(object):
    def __init__(self,length):
        self.head = None
        self.sizelen = length

    def creatlink(self,data):
        cur = CreatNode(data)
        self.head = tail = cur
        for i in range(1,self.sizelen):
            da = int(input('please input your node data:'))
            cur = CreatNode(da)
            tail.next = cur
            tail = tail.next
        return self.head
#---------------------------------------------------------------------------------
class funcation():
    def __init__(self, head):
        self.head = head

    def isEmpty(self):
        if self.head:
            print('Your link isn\'t empty!')
        else:
            print('Your link is empty!')

    def length(self):
        length = 0
        cur = self.head
        while cur:
            length += 1
            cur = cur.next
        return length

    def travel(self):
        cur = self.head
        while cur:
            print(cur.data,'->',end=' ')
            cur = cur.next
        print('None')

    def add_start(self, data):
        cur = CreatNode(data, self.head)
        self.head = cur
        return self.head

    def add_end(self, data):
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = CreatNode(data,None)
        return self.head

    def insert(self, node, index):
        prior = self.head
        inheritor = None

        while index - 1:
            inheritor = prior
            prior = prior.next
            index -= 1

        prior.next = node
        node.next = inheritor
        return self.head

    def pop(self, index):
        inheritor = self.head   #后继
        prior = None    #前驱

        if index == 1:
            self.head = self.head.next
        #elif index - 1 == self.length(self.head): 调用自己类中的方法  也可以类名.方法() 此处不这样在单独列出结尾的处理了，因为和处理中间位置同理
        else:
            while index - 1:
                prior = inheritor
                inheritor = inheritor.next
                index -= 1

            prior.next = inheritor.next
        return self.head

    def reverse(self):
        new = self.head
        self.head = self.head.next
        new.next = None
        cur = self.head
        while cur:
            p = cur
            cur = cur.next
            p.next = new
            new = p
        return new

if __name__ == '__main__':
    length = int(input('input the length of link: '))
    link = CreatLink(length)
    data = int(input('please input your node data:'))
    head = link.creatlink(data) #创建链表
    #----------------------------------------------------------------
    s = funcation(head)
    s.travel()  #遍历链表
    print('-'*32)

    head = s.reverse()  #逆序链表
    s = funcation(head)
    s.travel()  #遍历逆序后的链表
    print('-'*32)

    count = s.length()  #统计链表长度
    print('your link length is :',count)
    index = int(input('please input your will delete node data:'))
    head = s.pop(index)  #删除指定位置的节点

    s = funcation(head)
    s.isEmpty() #判断链表是否为空
    s.travel()  #遍历删除节点后的链表
    #添加节点

    print('-'*32)
    head = s.add_end(10)
    s = funcation(head)
    s.travel()