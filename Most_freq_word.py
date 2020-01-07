for i in range(int(input())):
    n=int(input())
    l=list(input().split())
    d1={}
    d2={}
    most,last=1,-1
    for x in l:
        if x in d1.keys():
            d1[x]+=1
        else:
            d1[x]=1
            d2[x]=l.index(x)
        if d1[x]>=most:
            most=d1[x]
    for x in d1.keys():
        if d1[x]==most and d2[x]>last:
            res=x
            last=d2[x]
    print(res)
