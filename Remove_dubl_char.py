for i in range(int(input())):
    l=input()
    s=''
    d={}
    for x in l:
        if x not in d.keys():
            d[x]=1
            s+=x
    print (s)