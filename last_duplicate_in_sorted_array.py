for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[x for x in a if a.count(x)>1]

    if len(b)==0:
        print(-1)
    else:
        for i in range(n-1,0,-1):
            if a[i]==b[-1]:
                print(i,a[i])
                break
