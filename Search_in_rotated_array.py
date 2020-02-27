'''Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element K. The task is to find the index of the given element K in the array A.

Input:
The first line of the input contains an integer T, denoting the total number of test cases. Then T test cases follow. Each test case consists of three lines. First line of each test case contains an integer N denoting the size of the given array. Second line of each test case contains N space separated integers denoting the elements of the array A. Third line of each test case contains an integer K denoting the element to be searched in the array.

Output:
Corresponding to each test case, output the index of the element found in the array.  If element is not present, then output -1.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
0 ≤ Ai ≤ 108
1 ≤ K ≤ 108

Example:
Input:
3
9
5 6 7 8 9 10 1 2 3
10
3
3 1 2
1
4
3 5 1 2
6

Output:
5
1
-1'''
def findpivot(arr,l,r):
    if l>r:
        return -1
    if l==r:
        return 1
    mid=(l+r)//2
    if arr[mid]>arr[mid+1]:
        return mid
    elif arr[mid-1]>arr[mid]:
        return mid-1
    elif arr[mid]<=arr[l]:
        return findpivot(arr,l,mid-1)
    else:
        return findpivot(arr,mid+1,r)
def binarysearch(arr,l,r,k):
    if l>r:
        return -1
    mid=(l+r)//2
    if arr[mid]==k:
        return mid
    elif arr[mid]>k:
        return binarysearch(arr,l,mid-1,k)
    else:
        return binarysearch(arr,mid+1,r,k)
def pivotedsearch(arr,l,r,k):
    pos=findpivot(arr,l,r)
    if pos==-1:
        return binarysearch(arr,l,r,k)
    if arr[pos]==k:
        return pos
    if arr[0]<=k:
        return binarysearch(arr,l,pos-1,k)
    else:
        return binarysearch(arr,pos+1,r,k)

    


for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=int(input())   
    print(pivotedsearch(l,0,n-1,k))
    l.clear()
