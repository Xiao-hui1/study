import sys
from asyncio.windows_events import INFINITE
from json.encoder import INFINITY

"""
    使用贪心算法解决找零问题
"""

def optimal_small(denom, total):
    sorted_denom = sorted(denom, reverse=True)
    series = []
    for i in range(len(sorted_denom)):
        term = sorted_denom[i:]
        number = []
        local = total
        for j in term:
            div = local//j
            local = local % j
            if div > 0:
                number.append((j, div))
        series.append(number)
    return series

s = optimal_small([1,3,5,7,9,20],86)
print(s)




"""
    利用贪心算法求出最短的路径
"""

class Path():
    def path(self):

        graph = dict()
        graph['A'] = {'A':5, 'D':9, 'E':2}
        graph['B'] = {'A':5, 'C':2}
        graph['C'] = {'B':2, 'D':3}
        graph['D'] = {'A':9, 'F':2, 'C':3}
        graph['E'] = {'A':2, 'F':3}
        graph['F'] = {'E':3, 'D':2}


        table = dict()
        tablle = {
            'A':[0,None],
            'B':[float('inf'),None],
            'C':[float('inf'),None],
            'D':[float('inf'),None],
            'E':[float('inf'),None],
            'F':[float('inf'),None]
        }
        distance = 0
        previous = 1
        infinity = float('inf')

    def get_shortest_distance(self,table, vertex):
        shortest_distance = table[vertex][0]
        return shortest_distance

    def set_shortest_distance(self,table, vertex, new_distance):
        table[vertex][0] = new_distance

    def set_previous_node(self,table, vertex, previous_node):
        table[vertex][0] = previous_node

    def get_distance(self,graph, first, second):
        return graph[first][second]

    def get_next_node(self,table, visited_node):
        unvisited_node = list(set(table.keys()).difference(set(visited_node)))
        assumed_min = table[unvisited_node[0]][0]
        min_vertex = unvisited_node[0]
        for vertex in unvisited_node:
            if table[vertex][0] < assumed_min:
                assumed_min = table[vertex][0]
                min_vertex = vertex
        return min_vertex

    def find_shortest_path(self, graph, table, origin):
        #存储已经访问了的节点
        visited = []
        current_node = origin
        start_node = origin
        while True:
            adjacent_nodes = graph[current_node]
            if not set(adjacent_nodes).issubset(set(visited)):
                unvisited = set(adjacent_nodes).difference(set(visited))
                for  vertex in unvisited:
                    distance = self.get_shortest_distance(table, vertex)
                    if distance == INFINITY and current_node == start_node:
                        total_distance = self.get_distance(graph, vertex, current_node)
                    else:
                        total_distance = self.get_shortest_distance(table, current_node) + self.get_distance(graph, current_node, vertex)
                    if total_distance < distance:
                        self.set_shortest_distance(table, vertex, total_distance)
                        self.set_previous_node(table, vertex, current_node)
            visited.append(current_node)
            if len(visited)== len(table.keys()):
                break
            current_node = self.get_next_node(table, visited)

