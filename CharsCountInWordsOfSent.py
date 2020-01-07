for i in range(int(input())):
    l=list(input().split())
    res=[]
    for x in l:
        res.append(len(x))
    print(*res)