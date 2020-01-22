def maxcomb(n, arr,k):
    table=[[0 for x in range(k+1)] for x in range(n+1)]
    for i in range(0, n+1):
        table[i][0]=1
    for i in range(1,n+1):
        for j in range(1,k+1):
            if arr[i-1]<=j:
                table[i][j]=table[i-1][j]+table[i][j-arr[i-1]]
            else:
                table[i][j]=table[i-1][j]
    return table[n][k]

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=int(input())
    print(maxcomb(n,l,k))