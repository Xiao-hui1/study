import sys

input = lambda: sys.stdin.readline().strip()  # 快速读取一行并去除首尾空白字符
import math

inf = math.inf

def I():
    return input()

def II():
    return int(input())

def MII():
    return map(int, input().split())

def LI():
    return input().split()

def LII():
    return list(map(int, input().split()))

def LFI():
    return list(map(float, input().split()))

def GMI():
    return map(lambda x: int(x) - 1, input().split())

from bisect import *
from heapq import *
from collections import deque, Counter, defaultdict
from itertools import permutations

sys.setrecursionlimit(300000)
mod = 998244353


def solve():
    n = II()
    ac = LII()
    for i in range(n):
        pass
