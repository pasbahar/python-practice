'''Given a sorted array A of size N. The array is rotated 'K' times. Find the value of 'K'. The array may contain duplicate elements.

Input:
The first line contains an integer T, depicting total number of test cases. T testcases follow. Each testcase contains two lines of input. The first line contains an integer N depicting the size of array. The next line contains elements of the array separated by spaces.

Output:
For each testcase, print the value of K.

Constraints:
1 <= T <= 100
1 <= N <=107
0 <= Ai <= 1018

Example:
Input
2
5
5 1 2 3 4
5
1 2 3 4 5
Output
1
0

Explanation:
Testcase1: 5 1 2 3 4. The original sorted array is 1 2 3 4 5. We can see that the array was rotated 1 times to the right.'''
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    flag=0
    for i in range(n-1):
        if l[i]>l[i+1]:
            flag=1
            print(i+1)
    if not flag:
        print(0)