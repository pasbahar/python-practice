for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    try:
        print(l.index(k)+1)
    except:
        print(-1)