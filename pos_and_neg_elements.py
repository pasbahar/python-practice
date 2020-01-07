for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    pos=[x for x in l if x>0]
    neg=[x for x in l if x<0]
    res=[]
    for j in range(n//2):
        res.append(pos[j])
        res.append(neg[j])
    print(*res)