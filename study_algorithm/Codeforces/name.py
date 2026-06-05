import sys

from numpy.ma.core import append

"""
    Khba正在写他女朋友的名字。他已经n
    立方体，每个立方体上都写着一个小写拉丁字母。它们排成一行，形成一串s
    .他女朋友的名字也是一串t
    ，由 组成n
    小写拉丁字母。
    为了证明爱意，他必须检查是否能重新排列绳子的字母s
    所以那就成了她的名字t
"""
num = int(input())
res = []
for i in range(num):
    x = int(input())
    name = []
    name.extend(input().split())
    if len(name[0]) !=len(name[1]) != x:
        res.append('no')
        continue
    if sorted(name[0]) == sorted(name[1]):
        res.append('yes')
    else:
        res.append('no')
for i in res:
    print(i)