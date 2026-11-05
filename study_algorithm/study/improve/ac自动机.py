import collections


class AhoCorasick:
    def __init__(self):
        self.root = {}

    def add_word(self, word):
        # 构建 Trie 树
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = True  # 标记单词结束

    def build_fail(self):
        # 构建 Fail 指针：BFS 逐层求每个节点失配时的回退位置
        queue = collections.deque()
        for char, child in self.root.items():
            child['fail'] = self.root  # 第一层节点的 fail 指向根
            queue.append(child)

        while queue:
            node = queue.popleft()
            for char, child in node.items():
                if char == '#' or char == 'fail':
                    continue  # 跳过结束标记和 fail 指针本身
                queue.append(child)
                fail = node['fail']
                while fail is not self.root and char not in fail:
                    fail = fail['fail']
                child['fail'] = fail[char] if char in fail else self.root

    def search(self, text):
        # 匹配过程，打印所有模式串出现的结束位置
        node = self.root
        for i, char in enumerate(text):
            while node is not self.root and char not in node:
                node = node['fail']  # 顺着失败指针回溯
            node = node.get(char, self.root)
            # 沿 fail 链检查所有以当前位置结尾的单词
            tmp = node
            while tmp is not self.root:
                if '#' in tmp:
                    print(f"在位置 {i} 找到单词")
                tmp = tmp['fail']


if __name__ == "__main__":
    ac = AhoCorasick()
    for word in ["he", "she", "his", "hers"]:
        ac.add_word(word)
    ac.build_fail()
    ac.search("ushers")