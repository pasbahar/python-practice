for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    lo,mid=0,0
    hi=n-1
    while mid<=hi:
        if l[mid]==0:
            l[lo],l[mid]=l[mid],l[lo]
            mid+=1
            lo+=1
        elif l[mid]==1:
            mid+=1
        else:
            l[hi],l[mid]=l[mid],l[hi]
            hi-=1
    print(*l)