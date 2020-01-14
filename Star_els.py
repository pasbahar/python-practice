for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    q=[]
    mini=-999999
    for x in range(n-1,-1,-1):
        if l[x]>mini:
            q.append(l[x])
            mini=l[x]
    q=q[::-1]
    print(*q)
    if max(l)==q[0] and l.count(q[0])==1:
        print(q[0])
    else:
        print(-1)