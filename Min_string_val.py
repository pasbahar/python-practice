for i in range(int(input())):
    s=input()
    k=int(input())
    d={}
    res,flag=0,0
    for x in s:
        if x in d.keys():
            d[x]+=1
        else:
            d[x]=1
    l=sorted(list(d.values()))
    sz=len(l)
    if sum(l)<=k:
        print(0)
        flag=1
    while(k>0 and not flag):
        j=sz-1
        while k>0:
            l[j]-=1
            j-=1
            k-=1
            if(l[j+1]+1!=l[j]):
                break
    if not flag:
        for x in l:
            res=res+x*x
        print(res)
