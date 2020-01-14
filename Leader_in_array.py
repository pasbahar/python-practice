for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    res=[]
    res.append(l[n-1])
    max=l[n-1]
    for x in range(n-2,-1,-1):
        if l[x]>=max:
            max=l[x]
            res.append(l[x])
    res=res[::-1]
    print(*res)

    