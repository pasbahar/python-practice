def findpivot(arr,l,r):
    if l>r:
        return -1
    if l==r:
        return 1
    mid=(l+r)//2
    if arr[mid]>arr[mid+1]:
        return mid
    elif arr[mid-1]>arr[mid]:
        return mid-1
    elif arr[mid]<=arr[l]:
        return findpivot(arr,l,mid-1)
    else:
        return findpivot(arr,mid+1,r)
def binarysearch(arr,l,r,k):
    if l>r:
        return -1
    mid=(l+r)//2
    if arr[mid]==k:
        return mid
    elif arr[mid]>k:
        return binarysearch(arr,l,mid-1,k)
    else:
        return binarysearch(arr,mid+1,r,k)
def pivotedsearch(arr,l,r,k):
    pos=findpivot(arr,l,r)
    if pos==-1:
        return binarysearch(arr,l,r,k)
    if arr[pos]==k:
        return pos
    if arr[0]<=k:
        return binarysearch(arr,l,pos-1,k)
    else:
        return binarysearch(arr,pos+1,r,k)

    


for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=int(input())   
    print(pivotedsearch(l,0,n-1,k))
    l.clear()
