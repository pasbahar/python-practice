'''Given a Binary Tree your task is to print the nodes which dont have a sibling node .You are required to complete the function printSibling. You should not read any input from stdin/console. There are multiple test cases. For each test case, this method will be called individually.

Input: The first line of input contains T, denoting the number of testcases. For each testcase there will be 2 lines. The first line contains the number of edges. The second line contains nodes(number of edges  + 1) data. The task is to complete the function printSibling which takes 1 argument, root of the Tree. The struct node has a data part which stores the data, pointer to left child and pointer to right child. There are multiple test cases. For each test case, this method will be called individually.

Output:
The function should print all the nodes separated by space which don't have sibling in the tree in sorted order if every node has a tree than print -1.

Note: The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.

Constraints:
1 <=T<= 30
1 <=Number of nodes<= 100
1 <=Data of a node<= 1000

Example:
Input
1
1
1 2 L

Output 
2

Explanation:
Testcase 1: In above example there is one  test case which represents a  tree with 2 nodes and 1 edge where root is 1, left child of 1 is 2 .'''
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
