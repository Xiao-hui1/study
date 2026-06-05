"""
    使用回溯的算法进行解题:
        思想是:看0 - i 是否为回文串,如果是则加入列表中并且开始的位置变更为i + 1,如果不是则i + 1.(注意单个字符一定是回文的)
        dfs(0)
         └─ "a" (回文)
             └─ dfs(1)
                 └─ "c"
                     └─ dfs(2)
                         ├─ "d" → dfs(3) → ...
                         ├─ "dd" → dfs(4) → ...
                         └─ "ddd" → dfs(5) →
                                 └─ "a" → dfs(6)
                                         ├─ "d" → dfs(7)
                                         │    └─ "d" → dfs(8)
                                         │           └─ "f" → ...
                                         │           └─ "fef" → ✅ → dfs(11) → ...
                                         └─ "ad" ❌, "add" ❌, ...
"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        path = []
        n = len(s)
        def match(i, start):
            if i == n:
                ans.append(path.copy())
                return
            if i < n - 1:
                match(i + 1, start)
            t = s[start: i + 1]
            if t == t[::-1]:
                path.append(t)
                match(i+1,i+1)
                path.pop()
        match(0,0)
        return ans