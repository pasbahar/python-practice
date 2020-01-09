for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    res=[]
    for j in range(n-1):
        res.append(max(l[j+1:n]))
    res.append(-1)
print(*res)