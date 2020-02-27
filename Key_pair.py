'''Given an array A of N positive integers and another number X. Determine whether or not there exist two elements in A whose sum is exactly X.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N and X, N is the size of array. The second line of each test case contains N integers representing array elements A[i].

Output:
Print "Yes" if there exist two elements in A whose sum is exactly X, else "No" (without quotes).

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 105
1 ≤ A[i] ≤ 105

Example:
Input:
2
6 16
1 4 45 6 10 8
5 10
1 2 4 3 6

Output:
Yes
Yes

Explanation:
Testcases 1: 10 and 6 are numbers making a pair whose sum is equal to 16.'''
for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    flag=0
    for x in l:
        if k-x in l and (k-x!=x or l.count(x)>1):
            print("Yes")
            flag=1
            break
    if flag==0:
        print("No")
