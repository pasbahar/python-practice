'''Given an unsorted array A of size N. Find the subarray A[s..e] such that sorting this subarray makes the whole array sorted.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, N is the size of array. The second line of each test case contains N elements.

Output:
Print the starting and ending index(0-based indexing) of subarray A[s..e]. If no such subarray exists, print 0 for starting index and 0 for ending index.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
1 ≤ C[i] ≤ 108

Example:
Input:
2
11
10 12 20 30 25 40 32 31 35 50 60
9
0 1 15 25 6 7 30 40 50

Output:
3 8
2 5

Explanation:
Testcase 1: Subarray starting from index 3 and ending at index 8 is required subarray.'''
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l1=sorted(l)
    s,e=n-1,0
    for j in range(1,n):
        if  l[j]!=l1[j]:
            s=j
            break
    if s==n-1 and n>1:
        print(0)
    else:
        for j in range(n-1,-1,-1):
            if l1[j]!=l[j]:
                e=j
                break
        print(s,e,end=" ")
        print()
        
