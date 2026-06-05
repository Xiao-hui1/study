t = int(input())
res = []

for i in range(t):
    s = int(input())
    ls = []
    for j in range(s):
        ls.append(input(""))
    val = []
    for idx, row in enumerate(ls):
        p = 0
        for j in row:
            if j =='.':
                p +=1
            elif j == '#':
                val.append(p+1)
    res.append(val)

for idx, row in enumerate(res):
    for i in range(len(row)-1,-1,-1):
        print(res[idx][i], end=' ')
    print()