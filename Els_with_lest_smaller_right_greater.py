'''Given an unsorted array of size N. Find the first element in array such that all of its left elements are smaller and all right elements to it are greater than it.

Note: Left and right side elements can be equal to required element. And extreme elements cannot be required element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated array elements.

Output:
For each test case, in a new line print the required element. If no such element present in array then print -1.

Constraints:
1 <= T <= 100
3 <= N <= 106
1 <= A[i] <= 106

Example:
Input:
3
4
4 2 5 7
3
11 9 12
6
4 3 2 7 8 9

Output:
5
-1
7
Explanation:
Testcase 1 : Elements on left of 5 are smaller than 5 and on right of it are greater than 5.'''
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    curr_m=l[0]
    flag=0
    for x in range(1,n-1):
        flag1=0
        if l[x]>=curr_m:
            for j in range(n-1,x,-1):
                if l[j]<l[x]:
                    flag1=1
                    break
            if flag1:
                curr_m=l[x]
            else:
                print(l[x])
                flag=1
                break
    if not flag:
        print(-1)