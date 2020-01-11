class Node:
    def __init__(self,val):
        self.left=None
        self.data=val
        self.right=None

def printSiblin(root):
    if root==None:
        return
    if root.right:
        printSiblin(root.right)
        if root.left is None:
            printSiblin.arr.append(root.right.data)
    if root.left:
        printSiblin(root.left)
        if root.right is None:
             printSiblin.arr.append(root.left.data)
    if root== printSiblin.node:
        if len( printSiblin.arr)==0:
            print(-1)
        else:
            printSiblin.arr=sorted(printSiblin.arr)
            print(* printSiblin.arr)
        printSiblin.node=None
        printSiblin.arr.clear()

for i in range(int(input())):
    root=None
    n=int(input())
    arr=input().strip().split()
    if n==0:
        print()
        continue
    root=None
    dictTree=dict()

    for j in range(n):
        if arr[3*j] not in dictTree:
            dictTree[arr[3*j]]=Node(int(arr[3*j]))
            parent=dictTree[arr[3*j]]
            if j==0:
                root=parent
        else:
            parent=dictTree[arr[3*j]]
        child=Node(int(arr[3*j])+1)

        if arr[3*j+2]=="L":
            parent.left=child
        else:
            parent.right=child
    printSiblin.arr=[]
    printSiblin.node=root
    printSiblin(root)
