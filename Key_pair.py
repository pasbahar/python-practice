for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    flag=0
    for x in l:
        if k-x in l and (k-x!=x or l.count(x)>1):
            print("Yes")
            flag=1
            break
    if flag==0:
        print("No")
