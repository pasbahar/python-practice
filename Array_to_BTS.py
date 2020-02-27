'''Given a sorted array. Write a program that creates a Balanced Binary Search Tree using array elements. If there are N elements in array, then floor(n/2)'th element should be chosen as root and same should be followed recursively.

Input:
The first line of input contains an integer T, denoting the number of test cases. The first line of each test case is N(size of array). The second line of each test case contains N input A[].

Output:
Print the preorder traversal of constructed BST.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 1000
1 ≤ A[i] ≤ 10000

Example:
Input:
1
7
1 2 3 4 5 6 7

Output:
4 2 1 3 6 5 7'''
class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.data=val

def ct(arr,start,end):
    if start>end:
        return None
    if start==end:
        return Node(arr[start])
    mid=(start+end)//2
    root=Node(arr[mid])
    root.left=ct(arr,start,mid-1)
    root.right=ct(arr,mid+1,end)
    return root

def preprint(root):
    if root is None:
        return
    print(root.data, end=" ")
    preprint(root.left)
    preprint(root.right)

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    tree=ct(l,0,n-1)
    preprint(tree)