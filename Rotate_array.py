for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(0,k):
        l.append(l[0])
        l.pop(0)
    print(*l)