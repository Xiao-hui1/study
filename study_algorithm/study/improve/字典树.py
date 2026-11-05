"""
        字典树：
            1.创建，利用数组来创建字典树，因为英文字母只有26个，所以每个节点数组的大小为26(下标对应着每个字母)，数组中存储着它的子节点层的位置下标。
            2.

"""
import sys

n = int(input())
total = 0

data = []
for i in range(n):
    word = input()
    data.append(word)
    total += len(word)

# 节点数最多为 total + 1（含根节点 0），数组必须开 total + 1
tree = [[0] * 26 for _ in range(total + 1)]
p = [0] * (total + 1)
e = [0] * (total + 1)

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

# 建完树后从标准输入读取查询，每行一个单词，输出以它为前缀的单词个数
for line in sys.stdin:
    line = line.strip()
    if line:
        print(find_pre(line))