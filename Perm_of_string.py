def permut(arr,l,r):
    if l==r:
        res.append("".join(arr))
    for x in range(l,r):
        arr[x],arr[l]=arr[x],arr[l]
        permut(arr,l+1,r)
        arr[x],arr[l]=arr[l],arr[x]

for i in range(int(input())):
    arr=list(input().rstrip())
    res=list()
    permut(arr,0,len(arr))
    res.sort()
    for x in res:
        print(x,end=" ")
    print()
    res=[]