from pyparsing import restOfLine

n = int(input())
res = []
for i in range(n):
    val = int(input())
    # if val // 2 % 2 == 0:
    if val <= 3:
        res.append(val)
    else:
        res.append(min(val % 2, val % 3))
    # else:
    #     if val % 2 == 0 or (val // 3 % 2 == 1 and 0 <= val % 3 <= 1):
    #         res.append(0)
    #     elif val // 3 % 2 == 0:
    #         res.append(min(val % 2, val % 3))
for i in res:
    print(i)