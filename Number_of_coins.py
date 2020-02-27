def coins(v,l):
    t=[10000 for x in range(v+1)] 
    t[0]=0
    for i in l:
        for j in range(1,v+1):
            if i<=j:
                t[j]=min(t[j],t[j-i]+1)
    if t[v]!=10000: return t[v]
    else: return -1 


for i in range(int(input())):
    v,n=map(int,input().split())
    l=list(map(int,input().split()))
    print(coins(v,l))