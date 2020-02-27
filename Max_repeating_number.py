'''Given an array A of size N, the array contains numbers in range from 0 to k-1 where k is a positive integer and k <= N. Find the maximum repeating number in this array. If there are two or more maximum repeating numbers print the element having least value.

Input:
The first line of input contains an integer T, denoting the number of test cases. T testcases follow. Each testcase contains two lines of input. First line contains N and k, both separated by a space. The next line contains N integers separated by spaces.

Output:
For each testcase, in a new line, print the maximum frequency element.

Constraints:
1 <= T <= 100
1 <= N <= 107
0 <= k <= N
0 <= Ai <= k-1

Example:
Input:

2
4 3
2 2 1 2
6 3
2 2 1 0 0 1
Output:
2
0

Explanation:

Testcase1: 2 is the most frequent element.
Testcase2: 0 1 and 2 all have same frequency of 2. But since 0 is smallest, we print that.'''
for i in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=[0 for i in range(b)]
    for j in range(a):
        d[c[j]]+=1
    max1=0
    for i in range(b):
        if (d[i]>d[max1]):
            max1=i
    print(max1)