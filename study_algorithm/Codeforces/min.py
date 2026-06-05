t = int(input())

ls = []
res = []
for i in range(t):
    ls.append(list(map(int, input().split())))
for idx,row in enumerate(ls):
    if row[0]-row[0] + row[1]-row[0] < row[1]-row[0] + row[1]-row[0]:
        res.append(row[0]-row[0] + row[1]-row[0])
    else:
        res.append(row[1]-row[0] + row[1]-row[1])

for i in res:
    print(i)