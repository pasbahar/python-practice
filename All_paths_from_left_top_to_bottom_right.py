'''The task is to count all the possible paths from top left to bottom right of a mXn matrix with the constraints that from each cell you can either move only to right or down.

Input: 
First line consists of T test cases. First line of every test case consists of N and M, denoting the number of rows and number of column respectively.

Output: 
Single line output i.e count of all the possible paths from top left to bottom right of a mXn matrix. Since output can be very large number use %10^9+7.

Constraints:
1<=T<=100
1<=N<=100
1<=M<=100

Example:
Input:
1
3 3
Output:
6'''
for i in range(int(input())):
    m,n=map(int,input().split())
    num=int(10**9+7)
    mat=[[1 for x in range(n)] for x in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            mat[i][j]=(mat[i-1][j]+mat[i][j-1])%num
    print(mat[m-1][n-1])
