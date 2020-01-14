for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    curr_m=l[0]
    flag=0
    for x in range(1,n-1):
        flag1=0
        if l[x]>=curr_m:
            for j in range(n-1,x,-1):
                if l[j]<l[x]:
                    flag1=1
                    break
            if flag1:
                curr_m=l[x]
            else:
                print(l[x])
                flag=1
                break
    if not flag:
        print(-1)