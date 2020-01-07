for i in range(int(input())):
    n=int(input())
    arr=sorted(list(map(int,input().split())))

    for r in range(n):
        arr[r]=arr[r]*arr[r]
    flag=0
    for j in range(n-1,1,-1):
        l=0
        r=j-1
        if flag:
            break
        while(l<r):
            if arr[l]+arr[r]==arr[j]:
                flag=1
                break
            elif arr[r]+arr[l]<arr[j]:
                l+=1
            else:
                r-=1
    if flag:
        print("YES")
    else:
        print("NO")

