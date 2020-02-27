'''Given two unsorted arrays A of size N and B of size M of distinct elements, the task is to find all pairs from both arrays whose sum is equal to X.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains 3 lines . The first line contains 3 space separated integers N, M, X. Then in the next two lines are space separated values of the array A and B respectively.

Output:
For each test case in a new line print the sorted space separated values of all the pairs u,v where u belongs to array A and v belongs to array B, such that each pair is separated from the other by a ',' without quotes also add a space after the ',' . If no such pair exist print -1.

Constraints:
1 <= T <= 100
1 <= N, M, X <= 106
-106 <= A, B <= 106

Example:
Input:
2
5 5 9
1 2 4 5 7
5 6 3 4 8
2 2 3
0 2
1 3
Output:
1 8, 4 5, 5 4
0 3, 2 1

Explanation:
Testcase 1: (1, 8), (4, 5), (5, 4) are the pairs which sum to 9.'''
def findpair(arr1,arr2,k):
    flag=0
    for i in arr1:
        if k-i in arr2:
            if not flag:
                flag=1
                print(i,end=" ")
                print(k-i,end="")
            else:
                print(',',i,end=' ')
                print(k-i,end="")
    if not flag: print(-1)
    else: print()



for i in range(int(input())):
    n1,n2,k=map(int,input().split())
    l1=sorted(list(map(int,input().split())))
    l2=list(map(int,input().split()))
    d2={}
    for i in l2:d2[i]=0
    findpair(l1,d2,k)