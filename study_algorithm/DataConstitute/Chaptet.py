from collections import deque
"""
    图的实现
"""
from pandas.core.common import maybe_iterable_to_list

graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['E', 'C','A']
graph['C'] = ['A', 'B','E','F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']

matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)
adjacency_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
edges_list = []
for key in matrix_elements:
    for value in graph[key]:
        edges_list.append((key, value))

#创建邻接矩阵

for edge in edges_list:
    index_of_first = matrix_elements.index(edge[0])
    index_of_last = matrix_elements.index(edge[1])
    adjacency_matrix[index_of_first][index_of_last] = 1

'''
    图的广度优先算法
        使用队列来进行处理
'''
def breadth_first_search(graph, root):
    #建立一个列表用来存储已经访问过了的节点。
    visited_vertices = list()
    #新建一个队列
    queue = deque([root])
    visited_vertices.append(root)
    node = root
    while len(queue) > 0:
        node = queue.popleft()
        adj_nodes = graph[node]
        #记录当前的这个节点的度中有哪些是还没有被访问过的。（使用的是集合中的求不同difference）
        remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        for elem in sorted(remaining_elements):
            #同时也将这些没有被访问过的节点放入到visi中，因为此入列的顺序和入队列的顺序是相同的所以进入visit的时间没有固定的要求
            visited_vertices.append(elem)
            #将未被访问的节点放入到队列中。
            queue.append(elem)

    return visited_vertices

"""
        图的深度优先算法
            使用栈来进行处理
"""
def depth_first_search(graph, root):

    visited_vertices = list()
    stack = list()
    stack.append(root)
    visited_vertices.append(root)
    node = root

    while len(stack) > 0:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adj_nodes = graph[node]
        if set(adj_nodes).issubset(set(visited_vertices)):  #判断当前的节点的相邻节点是否都已经被访问过了
            stack.pop()         #从栈中移除已经完成的节点
            if len(stack) > 0:
                node = stack[-1]    #对另一个分支进行遍历。
            continue
        else:
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        first_adj_nodes = sorted(remaining_elements)[0]
        stack.append(first_adj_nodes)
        print(stack)
        node  = first_adj_nodes
    return visited_vertices




"""
        优先队列的实现
"""

class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def arrange(self, k):
        #对新加入堆的数据进行处理，确保在最大的在最后。
        while k//2 > 0:
            if self.heap[k] < self.heap[k//2]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k //= 2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)

    def min_index(self, k):
        if k * 2 + 1 > self.size:
            return k * 2
        elif self.heap[k*2] < self.heap[k*2+1]:
            return k * 2
        else:
            return k * 2 + 1

    def sink(self, k):
        #把值较大的数据放到下面
        while k * 2 < self.size:
            mi = self.min_index(k)
            if self.heap[mi] < self.heap[k]:
                self.heap[k], self.heap[mi] = self.heap[mi], self.heap[k]
            k = mi

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item



if __name__ == '__main__':
    graph = dict()
    graph['A'] = ['B', 'C']
    graph['B'] = ['E', 'C', 'A']
    graph['C'] = ['A', 'B', 'E', 'F']
    graph['E'] = ['B', 'C']
    graph['F'] = ['C']
    ans = breadth_first_search(graph, 'A')

    res = depth_first_search(graph, 'A')
    print(ans)
    print(res)

    # h = Heap()
    # for i in (4,8, 7, 2, 9, 10, 5, 1, 3, 6):
    #     h.insert(i)
    # print(h.heap)
    # for i in range(10):
    #     n = h.pop()
    #     print(n)
    #     print(h.heap)