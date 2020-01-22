for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    arr,res=[],[]
    for i in range(0,2*n,2):
        arr.append([l[i],l[i+1]])
    arr.sort(key=lambda x:x[0])
    temp=arr[0][1]
    res.append([arr[0][0],arr[0][1]])
    for i in range(1,n):
        if arr[i][0]>temp:
            temp=arr[i][1]
            res.append([arr[i][0],arr[i][1]])
        elif res[-1][1]<arr[i][1]:
            res[-1][1]=arr[i][1]
    for i in range(len(res)):
        print(res[i][0],res[i][1],end=" ")
    print()


