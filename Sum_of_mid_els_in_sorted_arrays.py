for i in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    res=[]
    l,r=0,0
    while l<n and r<n:
        if l1[l]<l2[r]:
            res.append(l1[l])
            l+=1
        else:
            res.append(l2[r])
            r+=1
    while l<n or r<n:
        if l<r:
            res.append(l1[l])
            l+=1
        else:
            res.append(l2[r])
            r+=1

    print(res[n]+res[n-1])
