for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    res=[0 for x in range(n)]
    for x in l:
        res[x-1]+=1
    print(*res)