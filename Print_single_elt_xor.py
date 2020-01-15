for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    res=0
    for i in l:
        res^=i
    print(res)