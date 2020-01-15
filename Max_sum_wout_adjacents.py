for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    inc=l[0]
    exc=0
    for i in range(1,n):
        excn=max(inc,exc)
        inc=exc+l[i]
        exc=excn
    print(max(inc,exc))