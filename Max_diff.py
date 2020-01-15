def maxdif(arr):
    res,mn=-1,arr[0]
    for i in arr:
        if mn>i:
            mn=i
        if res<i-mn:
            res=i-mn
    return res

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(maxdif(l))