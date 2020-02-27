'''Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.

Input:
The first line contains an integer 'T' denoting the total number of test cases. Then T testcases follow. Each testcases contains two lines of input. The first line denotes the size of the array N. The second lines contains the elements of the array A separated by spaces.

Output: 
For each testcase, print the sorted array.

Constraints:
1 <= T <= 500
1 <= N <= 106
0 <= Ai <= 2

Example:
Input :
2
5
0 2 1 2 0
3
0 1 0

Output:
0 0 1 2 2
0 0 1'''
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    lo,mid=0,0
    hi=n-1
    while mid<=hi:
        if l[mid]==0:
            l[lo],l[mid]=l[mid],l[lo]
            mid+=1
            lo+=1
        elif l[mid]==1:
            mid+=1
        else:
            l[hi],l[mid]=l[mid],l[hi]
            hi-=1
    print(*l)