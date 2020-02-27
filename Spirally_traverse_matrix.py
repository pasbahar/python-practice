'''Given a matrix mat[][] of size M*N. Traverse and print the matrix in spiral form.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test cases follow. Each testcase has 2 lines. First line contains M and N respectively separated by a space. Second line contains M*N values separated by spaces.

Output:
Elements when travelled in Spiral form, will be displayed in a single line.

Constraints:
1 <= T <= 100
2 <= M,N <= 10
0 <= Ai <= 100

Example:
Input:
2
4 4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
3 4
1 2 3 4 5 6 7 8 9 10 11 12

Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
1 2 3 4 8 12 11 10 9 5 6 7'''
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
        
