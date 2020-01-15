for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l1=sorted(l)
    s,e=n-1,0
    for j in range(1,n):
        if  l[j]!=l1[j]:
            s=j
            break
    if s==n-1 and n>1:
        print(0)
    else:
        for j in range(n-1,-1,-1):
            if l1[j]!=l[j]:
                e=j
                break
        print(s,e,end=" ")
        print()
        
