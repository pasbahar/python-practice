for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l1=sorted(l)
    for i in l:
        if i<=l1[k-1]:
            print(i,end=" ")
