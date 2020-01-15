for i in range(int(input())):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    k=int(input())
    mat=[[0 for x in range(m)] for x in range(n)]
    flag=1
    n=-1
    for i in range(n):
        for j in range(m):
            mat[i][j]=l[i*m+j]
    for i in range(n):
        if k>=mat[i][0] and k<=mat[i][m-1]:
            ind=i
    if ind!=-1:
        for j in range(m):
            if mat[ind][j]==k:
                print(1)
                flag=0
                break
    if flag:
        print(0)