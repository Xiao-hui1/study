#part one:
import os
import sys

# 请在此输入您的代码
#
# i = int(input(""))
# num = []
# pre, tail = 0, 0
# # val = [[0]*i]*2
# for x in range(i):
#     v = input("")
#     v = v.split(" ")
#     vi = [int(y) for y in v]
#     num.append(vi)
#
# max0 = min0 = num[0][0]
# max1 = min1 = num[0][0]
#
# for x in range(i):
#     for y in range(i):
#         if x == y:
#
#             if num[x][y] > max0:
#                 max0 = num[x][y]
#             if num[x][y] < min0:
#                 min0 = num[x][y]
#
#         elif x + y == i - 1:
#
#             if num[x][y] > max1:
#                 max1 = num[x][y]
#             if num[x][y] < min1:
#                 min1 = num[x][y]
#
# max = max(max0, max1)
# min = min(min0, min1)
#
# print(max, min)

#part two:
import os
import sys

# 请在此输入您的代码
S = input("")
val = S[len(S)-1]
s = val +S[0:len(S)-1]
na = S + 'a'
siz = len(na)-1
num = 97
while na[siz] < 'z':
  na = na[0:len(na)-1] + chr(num)
  num += 1
  if na > S and na > s:
    print(na)
    break
#part four
import os
import sys

# 请在此输入您的代码
S = input("")
n =len(S)
s = S[::-1]
max_str = S if S > s else s

cand = max_str + 'a'
na = list(max_str)
found = False

for i in range(len(na)-1, -1, -1):
  if na[i] !='z':
    na[i]=chr(ord(na[i])+1)
    for j in range(i+1,len(na)):
      na[j] = 'a'
    cand1 = ''.join(na)
    Found = True
    break

if not found:
  print(cand)
else:
  print(min(cand1,cand))