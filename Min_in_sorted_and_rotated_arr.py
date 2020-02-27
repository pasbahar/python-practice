'''A sorted array A[ ] with distinct elements is rotated at some unknown point, the task is to find the minimum element in it.

Expected Time Complexity: O(Log n)

Input:

The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines. The first line of each test case consists of an integer N, where N is the size of array.
The second line of each test case contains N space separated integers denoting array elements.

Output:
Corresponding to each test case, in a new line, print the minimum element in the array.

Constraints:

1 ≤ T ≤ 200
1 ≤ N ≤ 500
1 ≤ A[i] ≤ 1000

Example:

Input
2
5
4 5 1 2 3
6
10 20 30 40 50 5 7

Output
1
5'''
def findmin(arr,l,r):
    if l>r:
        return arr[0]
    if l==r:
        return arr[l]
    mid=(l+r)//2
    if arr[mid]>arr[mid+1]:
        return arr[mid+1]
    if arr[mid]<arr[mid-1]:
        return arr[mid]
    if arr[mid]<arr[mid+1]:
        return findmin(arr,mid+1,r)
    return findmin(arr,l,mid-1)

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(findmin(l,0,n-1))