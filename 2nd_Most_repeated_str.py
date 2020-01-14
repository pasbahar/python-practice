import operator
for i in range(int(input())):
    n=int(input())
    l=list(input().split())
    d={}
    res=[]
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=0
    res=sorted(d.items(),key=operator.itemgetter(1))
    print(res[len(res)-2][0])
