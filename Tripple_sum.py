for i in range(int(input())):
    n,k=map(int,input().split())
    l=sorted(list(map(int,input().split())))
    flag=0
    for x in range(n):
        if flag==1:
            break
        lo=x+1
        r=n-1
        while(lo<r):
            if l[x]+l[lo]+l[r]<k:
                lo+=1
            elif l[x]+l[lo]+l[r]>k:
                r-=1
            else:
                flag=1
                print(1)
                break
    if not flag:
        print(0)


