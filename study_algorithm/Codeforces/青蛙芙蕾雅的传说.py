for _ in range(int(input())):
    x,y,k = map(int,input().split())
    print(max(2*((x+k-1)//k)-1,2*((y+k-1)//k)))