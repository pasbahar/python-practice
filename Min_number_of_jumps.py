def minjumps(n,l):
    if l[0]==0:
        return -1
    jumps=[0]*n
    for i in range(1,n):
        for j in range(i):
            if l[j]>=i-j:
                if jumps[i]!=0:
                    jumps[i]=min(jumps[i],jumps[j]+1)
                else:
                    jumps[i]=jumps[j]+1
    if jumps[-1]: return jumps[-1]
    else:
        return -1
        

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(minjumps(n,l))