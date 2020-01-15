for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    sm=0
    s,e=1,0
    for i in range(n):
        if sm<k:
            sm+=l[i]
        if sm>k:
            while sm>k:
                sm-=l[s-1]
                s+=1
        if sm==k:
            e=i+1
            print(s,e,end=" ")
            print()
            break
    if not e:
        print(-1)


