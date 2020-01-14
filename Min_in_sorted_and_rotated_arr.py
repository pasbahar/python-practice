def findmin(arr,l,r):
    if l>r:
        return arr[0]
    if l==r:
        return arr[l]
    mid=(l+r)//2
    if arr[mid]>arr[mid+1]:
        return arr[mid+1]
    if arr[mid]<arr[mid-1]:
        return arr[mid]
    if arr[mid]<arr[mid+1]:
        return findmin(arr,mid+1,r)
    return findmin(arr,l,mid-1)

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(findmin(l,0,n-1))