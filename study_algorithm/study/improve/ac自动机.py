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
        # 构建 Fail 指针 (简化版逻辑)
        queue = collections.deque()
        for char, child in self.root.items():
            queue.append((child, self.root))  # (当前节点, 父节点)

        while queue:
            node, parent = queue.popleft()
            # 这里省略了复杂的 fail 赋值逻辑，实际实现需递归查找
            for char, child in node.items():
                queue.append((child, node))

    def search(self, text):
        # 匹配过程
        node = self.root
        for i, char in enumerate(text):
            # 如果字符不在当前节点的子节点中
            while char not in node and node is not self.root:
                # node = node.fail # 顺着失败指针回溯 (伪代码)
                pass
            if char in node:
                # node = node[char] # 走到下一个节点 (伪代码)
                pass
            # 检查当前节点是否包含单词结尾
            if '#' in node:
                print(f"在位置 {i} 找到单词")