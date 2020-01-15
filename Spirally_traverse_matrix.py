for i in range(int(input())):
    m,n=map(int,input().split())
    l=list(map(int,input().split()))
    mat=[[0 for x in range(n)] for x in range(m)]
    k=0
    rs,re,cs,ce=0,n,0,m
    for i in range(m):
        for j in range(n):
            mat[i][j]=l[k]
            k+=1
    st=0
    while 1:
        if st<n*m:
            for it in range(rs,re,1):
                print(mat[cs][it],end=" ")
                st+=1
            cs+=1
        if st<n*m:
            for it in range(cs,ce,1):
                print(mat[it][re-1],end=" ")
                st+=1
            re-=1
        if st<n*m:
            for it in range(re-1,rs-1,-1):
                print(mat[ce-1][it],end=" ")
                st+=1
            ce-=1
        if st<n*m:
            for it in range(ce-1,cs-1,-1):
                print(mat[it][rs],end=" ")
                st+=1
            rs+=1
        if st>=n*m:
            break
    print()
        
