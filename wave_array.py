for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for x in range(0,n-1,2):
        l[x],l[x+1]=l[x+1],l[x]
    print(*l)