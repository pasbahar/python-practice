for i in range(int(input())):
    n,k=map(int,input().split())
    arr=sorted(list(map(int,input().split())))
    for j in range(n-1,n-k-1,-1):
        print(arr[j],end=" ")
    print()