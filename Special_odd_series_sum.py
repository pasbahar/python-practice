for i in range(int(input())):
    n=int(input())
    res,x=0,1
    for i in range(n,0,-1):
        res=res+x*i
        x+=2
    print(res)