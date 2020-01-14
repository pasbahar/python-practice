def isprime(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2,int(n**0.5)+1,1):
        if n%i==0:
            return False
    return True


for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    d={}
    res=[]
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d.keys():
        if isprime(d[i]) and d[i]>=k:
            res.append(i)
    res.sort()
    if len(res):
        print(*res)
    else:
        print(-1)
