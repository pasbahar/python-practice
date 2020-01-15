for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=int(input())
    try:
        print(l.index(k))
    except:
        print(-1)