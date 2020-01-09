for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    try:
        print(l.index(1))
    except:
        print(-1)