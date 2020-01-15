for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    res=[]
    for i in l:
        if len(res):
            if res[-1]==i:
                res[-1]*=2
                i=0
        if i:
            res.append(i)
        else:count+=1
    for i in range(count):
        res.append(0)       
    print(*res)
