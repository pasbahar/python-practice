def dotprod(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    table=[[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(1,m+1):
        for j in range(i,n+1):
            table[i][j]=max(table[i-1][j-1]+arr1[j-1]*arr2[i-1],table[i][j-1]);
    return table[m][n]

for i in range(int(input())):
    n,n1=map(int,input().split())
    l=list(map(int,input().split()))
    l1=list(map(int,input().split()))
    print(dotprod(l,l1))
