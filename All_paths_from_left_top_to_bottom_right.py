for i in range(int(input())):
    m,n=map(int,input().split())
    num=int(10**9+7)
    mat=[[1 for x in range(n)] for x in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            mat[i][j]=(mat[i-1][j]+mat[i][j-1])%num
    print(mat[m-1][n-1])
