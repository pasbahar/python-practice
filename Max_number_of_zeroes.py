for i in range(int(input())):
    n=int(input())
    l=list(map(str,input().split()))
    max_c=0
    res='-1'
    for x in l:
        count=0
        for j in x:
            if j=='0':
                count+=1
        if max_c<count:
            max_c=count
            res=x
        elif max_c==count and max_c!=0:
            if int(x)>int(res):
                res=x
    print(res)



