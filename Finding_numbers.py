for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    d={}
    for i in l:
        if i in d:
            d.pop(i)
        else: d[i]=0
    for i in sorted(d.keys()):
        print(i,end=" ")
    print()    
    
