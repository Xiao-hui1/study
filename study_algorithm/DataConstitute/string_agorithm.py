import hashlib
import sys, time

import numpy as np

"""
    字符串算法
        1.蛮力算法：
            逐个匹配直到字符串结尾
        2.Rabin-Karp算法  
            利用哈希表来进行匹配，如果哈希值相同，在判断是否字符串内容也完全相同，避免出现哈希值相同，内容不同的情况。
        3.Kunth-Morris-Pratt(KMP)算法：
            使用一个next数组来进行记录模拟的值,在模拟的过程中通过前缀和后缀是否相同来进行记录,例如:
                a   c   a   c   a   b
                0   0   1   2   3   0
        4.Boyer-Moore算法

"""

class RabinKarp(object):

    def generate_hash(self, text, pattern):
        text_len = len(text)
        pattern_len = len(pattern)
        ord_text = [ord(x) for x in text]
        ord_pattern = [ord(x) for x in pattern]
        hash_pattern = sum(ord_pattern)
        hash_len = text_len - pattern_len + 1
        text_hash = [0] * hash_len
        for i in range(hash_len):
            if i == 0:
                text_hash[i] = sum(ord_text[i:i + pattern_len])
            else:
                text_hash[i] = text_hash[i - 1] - ord_text[i - 1] + ord_text[i + pattern_len - 1]
        return [hash_pattern, text_hash]

    def Rabin_Karp_Matcher(self, text, sub):
        text = str(text)
        sub = str(sub)
        hash_pattern, text_hash = self.generate_hash(text, sub)
        flag = False
        for i in range(len(text_hash)):
            if hash_pattern == text_hash[i]:
                count = 0
                for j in range(len(sub)):
                    if sub[j] == text[i + j]:
                        count += 1
                    else:
                        break
                if count == len(sub):
                    flag = True
                    print("Pattern occours at index", i)
        if not flag:
            print("Pattern is not at all present in the text")



class KunthMorrisPratt:

    def pfun(self, pattern):
        n = len(pattern)
        prefix_fun = [0 for _ in range(n)]
        length = 0
        i = 1
        while i < n:
            if pattern[i] == pattern[length]:
                length += 1
                prefix_fun[i] = length
                i += 1
            else:
                if length != 0:
                    length = prefix_fun[length - 1]
                else:
                    prefix_fun[i] = 0
                    i = i + 1
        print(prefix_fun)
        return prefix_fun

    def KMP_Matcher(self, text, pattern):
        m = len(text)
        n = len(pattern)

        if n == 0:
            print("pattern is empty!")
            return

        flag = False
        prefix_fun = self.pfun(pattern)
        i = 0   #text的索引
        j = 0   #pattern的索引
        while i < m:
            if pattern[j] == text[i]:
                i += 1
                j += 1

            if j == n:
                print("Pattern occours with shift ", i-j)
                flag = True
                j = prefix_fun[j - 1]
            elif i < m and pattern[j] != text[i]:
                if j != 0:
                    j = prefix_fun[j - 1]
                else:
                    i += 1

        if not flag:
            print("Pattern is not at all present in the text")


class BoyerMoore:
    """
        坏字符于好后缀的结合.
    """
    def compute_bad_char_shift(self, sub):
        shift = {}
        for i, char in enumerate(sub):
            shift[char] = i
        print(shift)
        return shift

    def z_function(self, s):
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return z

    def compute_good_suffix_shift(self, sub):
        sl = len(sub)
        if sl == 0:
            return [0]
        gs_shift = [0] * sl
        reversed_sub = sub[::-1]
        Z = self.z_function(reversed_sub)[::-1]

        # 第一类：找到相同的后缀子串
        for i in range(sl - 1):
            suffix_len = Z[i]
            if suffix_len > 0:
                pos = sl - 1 - Z[i]
                if pos < sl - 1:
                    gs_shift[pos] = sl - 1 - i

        # 第二类：寻找最长公共前后缀作为回退
        for i in range(sl - 1):
            for k in range(1, sl):
                if sub.endswith(sub[:k]):
                    gs_shift[i] = sl - k
                    break
        return gs_shift

    def search1(self, text, sub):
        if not sub or len(sub) > len(text):
            print("matched_indexes: []")
            return

        sl = len(sub)
        bad_char_shift = self.compute_bad_char_shift(sub)
        # good_suffix_shift = self.compute_good_suffix_shift(sub)  # 可选启用

        matched_indexes = []
        i = 0

        while i <= len(text) - sl:
            j = sl - 1
            while j >= 0 and sub[j] == text[i + j]:
                j -= 1

            if j < 0:
                matched_indexes.append(i)
                i += 1
            else:
                t_char = text[i + j]
                bc_offset = j - bad_char_shift.get(t_char, -1)
                if t_char not in bad_char_shift:
                    bc_offset = j + 1
                i += max(1, bc_offset)

        print("matched_indexes:", matched_indexes)


    """
        坏字符的匹配.
    """
    def search2(self, text, sub):
        if not sub:  # 空模式串
            print("matched_indexes: []")
            return
        if len(sub) > len(text):  # 模式比文本长
            print("matched_indexes: []")
            return

        # 预处理：构建坏字符跳跃表
        # 对每个字符，记录其在模式中最右出现的位置
        bad_char_shift = {}
        for i, char in enumerate(sub):
            bad_char_shift[char] = i  # 记录最右边的位置

        l = len(text)
        sl = len(sub)
        matched_indexes = []
        i = 0  # 当前模式在文本中的偏移量

        while i <= l - sl:
            j = sl - 1  # 从模式最后一个字符开始比较

            # 从右往左逐个匹配
            while j >= 0 and sub[j] == text[i + j]:
                j -= 1

            # 如果完全匹配
            if j < 0:
                matched_indexes.append(i)
                i += 1  # 找到一次匹配后向右滑动一位（也可优化）
            else:
                # 发生不匹配，查看文本中对应的字符
                t_char = text[i + j]
                # 根据坏字符规则计算跳跃距离
                if t_char in bad_char_shift:
                    bc_shift = j - bad_char_shift[t_char]
                else:
                    bc_shift = j + 1
                i += max(1, bc_shift)  # 至少前进一格

        print("matched_indexes:", matched_indexes)




if __name__ == '__main__':
    # text = input()
    # sub = input()
    # rk = RabinKarp()
    # rk.Rabin_Karp_Matcher(text, sub)

    s = KunthMorrisPratt()
    s.KMP_Matcher('aaabcaacaabaacaadaabaabac', 'acacaa')
    print('-'*32*2)
    b = BoyerMoore()
    b.search1("aaabcaacaabaacaadaabaabac", "abcaa")