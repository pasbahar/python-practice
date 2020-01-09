def check(l1,l2):
    d1,d2={},{}
    for i in l1:
        if  i in d1.keys():
            d1[i]+=1
        else:
            d1[i]=1
    for i in l2:
        if  i in d2.keys():
            d2[i]+=1
        else:
            d2[i]=1
    for i in d1.keys():
        if i not in d2.keys() or d2[i]!=d1[i]:
            return(0)
    return(1)


for i in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    print(check(l1,l2))

