'''Given an array, the task is to print K smallest elements from the array but they must be in the same order as they are in given array.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains two Integers N and K and the second line contains N space separated elements.

Output:
For each test case, print the K smallest elements in new line.

Constraints:
1<=T<=100
1<=K<=N<=106
1<=A[i]<=105

Example:
Input:
2
5 2
5 4 2 1 2
7 5
1 2 3 4 5 6 7
Output:
2 1
1 2 3 4 5'''
for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l1=sorted(l)
    for i in l:
        if i<=l1[k-1]:
            print(i,end=" ")
