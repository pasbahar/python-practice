for i in range(int(input())):
    n=int(input())
    s=input()
    d={}
    flag=0
    for x in s:
        if x in d:
            d[x]+=1
        else:
            d[x]=1
    for x in s:
        if d[x]==1:
            print(x)
            flag=1
    if not flag:
        print(-1)
