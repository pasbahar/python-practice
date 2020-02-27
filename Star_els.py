'''Given an unsorted array. The task is to find all the star and super star elements in the array. Star are those elements which are strictly greater than all the elements on its right side. Super star are those elements which are strictly greater than all the elements on its left and right side.

Note: Assume first element (A[0]) is greater than all the elements on its left side, And last element (A[n-1]) is greater than all the elements on its right side.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, print the space separated star elements and then in new line print super star elements. If no super star element present in array then print "-1".

Constraints:
1<=T<=200
1<=N<=106
1<=A[i]<=106

Example:
Input:
2
6
4 2 5 7 2 1
3
8 6 5

Output:
7 2 1
7
8 6 5
8'''
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    q=[]
    mini=-999999
    for x in range(n-1,-1,-1):
        if l[x]>mini:
            q.append(l[x])
            mini=l[x]
    q=q[::-1]
    print(*q)
    if max(l)==q[0] and l.count(q[0])==1:
        print(q[0])
    else:
        print(-1)