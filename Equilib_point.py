for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    r=sum(l)
    left,flag=0,0
    for x in range(n):
        r-=l[x]
        if left==r:
            flag=1
            print(x+1)
        else:
            left+=l[x]
    if flag==0:
        print(-1)