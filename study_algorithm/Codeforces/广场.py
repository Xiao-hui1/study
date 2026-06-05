import math
"""
    判断一个n*m的矩阵的边的值的和是否相等
    每一行行求当前行的长度-1个数的和
"""
num = int(input())
val = []
for i in range(num):
    val.append(list(map(int, input().split())))
# post = []
# post.append(sum(val[0]))
# post.append(sum(val[num-1]))
# s_sum = e_sum = 0
# for j in range(num):
#     s_sum += val[j][0]
#     e_sum += val[j][3]
# post.append(s_sum)
# post.append(e_sum)
#
# if post[0]-val[0][3] == post[3]-val[num-1][3] == post[2] - val[0][0] == post[1] - val[num-1][0]:
#     print('yes')
# elif post[0]-val[0][0] == post[3]-val[0][3] == post[2] - val[0][num-1] == post[1] - val[num-1][3]:
#     print('yes')
# else:
#     print('no')
res = []
for idx,row in enumerate(val):
    for i in range(3):
        if val[idx][i] != val[idx][i+1]:
            res.append('no')
            break
        elif i == 2:
            res.append('yes')
for i in res:
    print(i)