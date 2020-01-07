for i in range(int(input())):
    n,k=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    res=0
    for j in range(n):
        times=k//l1[j]
        points=times*l2[j]
        if res<points:
            res=points
    print(res)
