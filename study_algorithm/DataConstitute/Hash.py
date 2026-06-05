"""
        哈希表 （也叫散列表）
        在哈希表中可能会存在哈希值的冲突，解决的办法有两种：
            1.线性探测  当前的哈希值在哈希表中已经有了元素了，则当前的元素先后进行探测，如果为空则将当前的值放入到，新找到的位置中
            2.二次探测  当前的哈希值在哈希标中已经有了元素，则先向后探测 1 个位置，如果该位置也有元素，则再向前探测 1 个位置，然后先后探测 2^2 个位置
                1^2,-1^2,2^2,-2^2,3^2,-3^2......
                按照此序列进行探测
            3.链接    当出现重复哈希值时，在同一个位置创建一个列表来，对这些具有相同哈希值的元素进行存储，
            但是列表在查找的时候速度比较慢，所有比较推荐使用BST二叉搜索树，但是要确保不是一个单支结构的树，需要保证是一个平衡树。

"""
class HashItem(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):
    def __init__(self):
        self.size = 256
        self.data = [None] * self.size
        self.count = 0  #统计哈希表中元素的个数。

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def _hash(self, key):
        mult = 1
        hv = 0
        for c in key:
            hv += ord(c) * mult
            mult += 1
        return hv % self.size

    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        while self.data[h] is not None:
            if self.data[h].key is  key:
                break
            h = (h + 1) % self.size

        if self.data[h] is None:
            self.count +=1
        self.data[h] = item

    def get(self, key):
        h = self._hash(key)
        while self.data[h] is not None:
            if self.data[h].key is key:
                return self.data[h].value
            h = (h + 1) % self.size
        return None



if __name__ == '__main__':
    h = HashTable()
    h['good'] = 'eggs'
    h['bad'] = 'spam'
    h['tabl'] = 'weapon'
    h['crew'] = 'proper'
    for key in ('good', 'bad', 'tabl', 'crew'):
        print(h[key])