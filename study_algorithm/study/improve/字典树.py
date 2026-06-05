from fontTools.t1Lib import stringToLong
"""
        字典树：
            1.创建，利用数组来创建字典树，因为英文字母只有26个，所以每个节点数组的大小为26(下标对应着每个字母)，数组中存储着它的子节点层的位置下标。
            2.

"""
n = int(input())
sum = 0

data = []
for i in range(n):
    str = input()
    data.append(str)
    sum += len(str)

tree = [[0] * 26 for _ in range(sum)]
p = [0] * sum
e = [0] * sum

idx = 0
def get_trie(s):
    global idx
    cur = 0
    p[cur] += 1

    for j in s:
        path = ord(j) - ord('a')
        if tree[cur][path] == 0:
            tree[cur][path] = idx + 1
            idx += 1
        cur = tree[cur][path]
        p[cur] += 1
    e[cur] += 1

def find(s) -> int:
    cur = 0
    for i in s:
        path = ord(i) - ord('a')
        if tree[cur][path] == 0:
            return 0
        cur = tree[cur][path]
    return e[cur]

def find_pre(s) -> int:
    cur = 0
    for i in s:
        path = ord(i) - ord('a')
        if tree[cur][path] == 0:
            return 0
        cur = tree[cur][path]
    return p[cur]

for i in range(n):
    get_trie(data[i])

print(find_pre('abc'))