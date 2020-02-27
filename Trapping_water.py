def trap(arr):
    res,l,r, max_l,max_r=0,0,len(arr)-1,0,0
    while(l<r):
        if arr[l]<arr[r]:
            if arr[l]>max_l:
                max_l=arr[l]
            else:
                res+=max_l-arr[l]
                l+=1
        else:
            if arr[r]>max_r:
                max_r=arr[r]
            else:
                res+=max_r-arr[r]
                r-=1
    return res

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(trap(l))
