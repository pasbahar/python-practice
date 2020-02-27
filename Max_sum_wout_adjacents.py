'''Given an array A of positive integers. Find the maximum sum of a subsequence such that no two numbers in the sequence should be adjacent in the array.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, size of array. The second line of each test case contains N elements.

Output:
Print the maximum sum of a subsequence.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106
1 ≤ Ci ≤ 107

Example:
Input:
2
6
5 5 10 100 10 5
4
3 2 7 10

Output:
110
13

Explanation:
Testcase 2 : 3 and 10 forms a non-continuous subsequence with maximum sum.'''
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    inc=l[0]
    exc=0
    for i in range(1,n):
        excn=max(inc,exc)
        inc=exc+l[i]
        exc=excn
    print(max(inc,exc))