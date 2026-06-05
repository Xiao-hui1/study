t = int(input())
res = [0]*t

for i in range(t):
    val = []
    s = int(input())        #接收坐标
    dp = [[0]*s for _ in range(s)]    #建立dp
    for j in range(s):      #接收
        val.append(list(map(int, input().split())))
    #判断是否为直角三角形
    for r in range(0,s-2):
        for c in range(r+1,s-1):
            for d in range(c+1,s):
                A = B = C = 0
                if  dp[c][r] or dp[r][c]:
                    A = dp[c][r]
                else:
                    A = dp[c][r] = (val[r][0]-val[c][0])**2 + (val[r][1]-val[c][1])**2

                if dp[d][c] or dp[c][d]:
                    B = dp[d][c]
                else:
                    B = dp[d][c] = (val[d][0]-val[c][0])**2 + (val[d][1]-val[c][1])**2

                if dp[d][r] or dp[r][d]:
                    C = dp[d][r]
                else:
                    C = dp[d][r] = (val[d][0]-val[r][0])**2 + (val[d][1]-val[r][1])**2

                if A + B == C or A + C == B or B + C == A:
                    res[i] += 1

for i in res:
    print(i)