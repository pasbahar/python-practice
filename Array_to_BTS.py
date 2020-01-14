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