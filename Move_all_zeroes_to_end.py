for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for x in l:
        if x==0:
            l.remove(x)
            l.append(0)
    print(*l)