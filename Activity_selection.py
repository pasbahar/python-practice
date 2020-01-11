import operator
for i in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    f=list(map(int,input().split()))
    d=[]
    count=1
    for x in range(n):
        d.append((s[x],f[x]))
    d.sort(key=operator.itemgetter(1))
    l=0
    for j in range(1,n):
        if d[l][1]<=d[j][0]:
            l=j
            count+=1
    print(count)
    