for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for x in range(n):
        l[x]=l[x]-x
    l.sort()
    print(l[-1]-l[0])