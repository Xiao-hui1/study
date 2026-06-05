# n = int(input())
# data = []
# for _ in range(n):
#     data.append(input())
# d = input().split()
# if data[int(d[0]) - 1] == d[1]:
#     print("Yes")
# else:
#     print("No")



# ----------------------------------
# x, y = map(int, input().split())
# for i in range(8):
#     t = y
#     y = int(str(x + y)[::-1])
#     x = t
# print(y)

# -------------------------------

def calc(s, start):
    pos = []
    for idx, c in enumerate(s):
        if c == 'A':
            pos.append(idx)
    res = 0
    for i in range(len(pos)):
        res += abs(pos[i] - (start + 2 * i))
    return res

n = int(input())
s = input().strip()
print(min(calc(s, 0), calc(s, 1)))


#---------------------------------------------
"""
        双向链表加，哈希表：
        
                初始序列 A = (0)，依次处理 Q 次查询：1 x：在x 后面插入数字 i（i 为当前是第几次查询）；2 x y：
            删除 x 和 y 之间的所有元素，输出被删元素的和，并将 x 与 y 直接相连。所有数字唯一，每个数字只出现一次。

"""
import sys

input = sys.stdin.read
data = input().split()


def main():
    idx = 0
    Q = int(data[idx])
    idx += 1

    # 双向链表
    prev = dict()
    next_ = dict()
    # 记录每个值存在哪里
    pos = dict()

    # 初始 A = [0]
    start = 0
    prev[0] = None
    next_[0] = None
    pos[0] = 0

    for i in range(1, Q + 1):
        cmd = int(data[idx])
        if cmd == 1:
            x = int(data[idx + 1])
            idx += 2

            # 在 x 后面插入 i
            nx = next_[x]
            prev[i] = x
            next_[i] = nx
            next_[x] = i
            if nx is not None:
                prev[nx] = i
            pos[i] = i
        else:
            x = int(data[idx + 1])
            y = int(data[idx + 2])
            idx += 3

            # 找到 x, y 的位置
            L = x
            R = y

            # 把 L 变成左边，R 变成右边
            # 遍历找到顺序
            cur = L
            while cur != R and cur is not None:
                cur = next_[cur]
            if cur != R:
                L, R = R, L

            # 计算 L 和 R 之间的和
            res = 0
            p = next_[L]
            while p != R:
                nxt_p = next_[p]
                res += p
                # 删除 p
                del prev[p]
                del next_[p]
                del pos[p]
                p = nxt_p

            # 连接 L 和 R
            next_[L] = R
            prev[R] = L
            print(res)


if __name__ == '__main__':
    main()