for i in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    res=[]
    left=0
    right=n-1
    while(left<right):
        if -l[left]>l[right]:
            left+=1
        elif -l[left]<l[right]:
            right-=1
        else:
            res.append(l[right])
            res.append(l[left])
            left+=1
            right-=1
    res=res[::-1]
    if len(res)==0:
        print(0)
    else:
        print(*res)
        
