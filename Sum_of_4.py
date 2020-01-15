def sumof4(arr,k,n):
    for i in range(n):
        for j in range(i+1,n):
            for l in range(j+1,n):
                for g in range(l+1,n):
                    sum=arr[i]+arr[j]+arr[l]+arr[g]
                    if sum==k:
                        return 1
                    elif sum>k:
                        break
                if arr[i]+arr[j]+arr[l]>k:break
            if arr[i]+arr[j]>k:break    
        if arr[i]>k:break
    return 0


for i in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    k=int(input())
    print(sumof4(l,k,n))