def maxdif(arr):
    res,mn=-1,1000000
    flag=0
    for i in arr:
        if mn>i:
            mn=i
        else:
            flag=1
        if res<i-mn:
            res=i-mn
    if flag:
        return res
    else:
        return -1

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(maxdif(l))