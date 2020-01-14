for i in range(int(input())):
    n1,n2,n3=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l3=list(map(int,input().split()))
    d={}
    res=[]
    for x in l1:
        if x in d:
            d[x]+=1
        else:
            d[x]=0
    for x in l2:
        if x in d:
            d[x]+=1
        else:
            d[x]=0
    for x in l3:
        if x in d:
            d[x]+=1
        else:
            d[x]=0
    for x in d.keys():
        if d[x]==2:
            res.append(x)
    res.sort()
    print(*res)