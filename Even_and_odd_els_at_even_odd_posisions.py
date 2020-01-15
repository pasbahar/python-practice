for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    res=[0 for x in range(n)]
    even,odd,j=0,1,0
    while(even<n and odd<n):
        if l[j]%2==0:
            res[even]=l[j]
            even+=2
        else:
            res[odd]=l[j]
            odd+=2
        j+=1
    while(even<n):
        res[even]=l[j]
        even+=2
        j+=1
    while(odd<n):
        res[odd]=l[j]
        odd+=2
        j+=1
    print(*res)

