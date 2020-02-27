'''Given a sorted array A, size N, of integers; every element appears twice except for one. Find that element that appears once in array.

Input:
The first line of input consists of T, the number of the test cases. T testcases follow. Each testcase contains two lines of input.
The first line of each test case contains the size of the array, and the second line has the elements of the array.

Output:
For each testcase, in a new line, print the number that appears only once in the array.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
0 ≤ A[i] ≤ 1017

Example:
Input:
1
11
1 1 2 2 3 3 4 50 50 65 65
Output:
4'''
def AppearOnce(l,n):
    if l[0]!=l[1]: return l[0]
    for i in range(1,n-1):
        if l[i-1]!=l[i] and l[i]!=l[i+1]: return l[i]
    if l[n-2]!=l[n-1]:return l[n-1]

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(AppearOnce(l,n))
