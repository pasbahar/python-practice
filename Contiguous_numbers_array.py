for i in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    flag=0
    for x in range(1,n):
        if  l[x]>l[x-1]+1:
            print("No")
            flag=1
            break
    if not flag:
        print('Yes')