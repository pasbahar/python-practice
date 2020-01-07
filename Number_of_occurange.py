for i in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    d={}
    for x in arr:
        if x in d.keys():
            d[x]+=1
        else:
            d[x]=1
    if k in d.keys():
        print(d[k])
    else:
        print(-1)