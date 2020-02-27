'''Given three increasingly sorted arrays A, B, C of sizes N1, N2, and N3 respectively, you need to print all common elements in these arrays.

Note: Please avoid printing the same common element more than once.

Input:
First line contains a single integer T denoting the total number of test cases. T testcases follow. Each testcase contains four lines of input. First line consists of 3 integers N1, N2 and N3, denoting the sizes of arrays A, B, C respectively. The second line contains N1 elements of A array. The third lines contains N2 elements of B array. The fourth lines contains N3 elements of C array.

Output:
For each testcase, print the common elements of array. If not possible then print -1.

Constraints:
1 <= T <= 100
1 <= N1, N2, N3 <= 107
1 <= Ai, Bi, Ci <= 1018

Example:
Input:
1
6 5 8
1 5 10 20 40 80
6 7 20 80 100
3 4 15 20 30 70 80 120
Output:
20 80

Explanation:
Testcase1:  20 and 80 are the only common elements'''
for i in range(int(input())):
    n1,n2,n3=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l3=list(map(int,input().split()))
    d={}
    res=[]
    for x in l1:
        if x in d:
            d[x]+=1
        else:
            d[x]=0
    for x in l2:
        if x in d:
            d[x]+=1
        else:
            d[x]=0
    for x in l3:
        if x in d:
            d[x]+=1
        else:
            d[x]=0
    for x in d.keys():
        if d[x]==2:
            res.append(x)
    res.sort()
    print(*res)