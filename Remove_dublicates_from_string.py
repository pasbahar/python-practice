for i in range(int(input())):
    s=input()
    d={}
    res=''
    for x in s:
        if x not in d:
            d[x]=0
            res+=x
    print(res)
