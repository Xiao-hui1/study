"""
分块算法（Sqrt Decomposition）—— 区间最大值
支持：
  - 区间查询最大值 query(l, r)   O(√n)
  - 单点修改 update(i, x)        O(1)
  - 区间加 add(l, r, x)          O(√n)   （懒标记版）

下标均为 0-based 闭区间 [l, r]。
"""
from math import isqrt


class SqrtDecomposition:
    def __init__(self, a):
        self.a = a[:]
        self.n = len(a)
        self.bsize = isqrt(self.n) + 1          # 块长
        self.nb = (self.n + self.bsize - 1) // self.bsize  # 块数
        self.bid = [i // self.bsize for i in range(self.n)]  # 每个位置所属块
        # 每块的左右端点
        self.bl = [b * self.bsize for b in range(self.nb)]
        self.br = [min(self.n - 1, (b + 1) * self.bsize - 1) for b in range(self.nb)]
        self.bmax = [max(a[l:r + 1]) for l, r in zip(self.bl, self.br)]
        self.lazy = [0] * self.nb               # 整块加法懒标记

    def _push(self, b):
        """把块 b 的懒标记下放到元素上"""
        if self.lazy[b]:
            for i in range(self.bl[b], self.br[b] + 1):
                self.a[i] += self.lazy[b]
            self.lazy[b] = 0

    def update(self, i, x):
        """单点赋值 a[i] = x"""
        b = self.bid[i]
        self._push(b)
        self.a[i] = x
        self.bmax[b] = max(self.a[self.bl[b]:self.br[b] + 1])

    def add(self, l, r, x):
        """区间 [l, r] 全部加 x"""
        lb, rb = self.bid[l], self.bid[r]
        if lb == rb:  # 同一块内直接暴力
            self._push(lb)
            for i in range(l, r + 1):
                self.a[i] += x
            self.bmax[lb] = max(self.a[self.bl[lb]:self.br[lb] + 1])
            return
        # 左侧不完整块
        self._push(lb)
        for i in range(l, self.br[lb] + 1):
            self.a[i] += x
        self.bmax[lb] = max(self.a[self.bl[lb]:self.br[lb] + 1])
        # 右侧不完整块
        self._push(rb)
        for i in range(self.bl[rb], r + 1):
            self.a[i] += x
        self.bmax[rb] = max(self.a[self.bl[rb]:self.br[rb] + 1])
        # 中间完整块直接打懒标记
        for b in range(lb + 1, rb):
            self.lazy[b] += x
            self.bmax[b] += x

    def query(self, l, r):
        """查询区间 [l, r] 最大值"""
        lb, rb = self.bid[l], self.bid[r]
        if lb == rb:
            return max(self.a[i] + self.lazy[lb] for i in range(l, r + 1))
        ans = max(self.a[i] + self.lazy[lb] for i in range(l, self.br[lb] + 1))
        ans = max(ans, max(self.a[i] + self.lazy[rb] for i in range(self.bl[rb], r + 1)))
        for b in range(lb + 1, rb):
            ans = max(ans, self.bmax[b])  # 懒标记已包含在 bmax 里
        return ans


if __name__ == "__main__":
    a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    sd = SqrtDecomposition(a)
    print(sd.query(0, 9))  # 9
    print(sd.query(2, 5))  # 9
    sd.update(6, 100)      # a[6] = 100
    print(sd.query(0, 9))  # 100
    sd.add(0, 3, 10)       # 前 4 个各加 10
    print(sd.query(0, 3))  # 14 (4+10)
    print(sd.query(4, 9))  # 100
