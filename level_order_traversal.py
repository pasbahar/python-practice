'''Given a Binary Tree, your task is to print its level order traversal such that each level is separated by $.
For the below tree the output will be 1 $ 2 3 $ 4 5 6 7 $ 8 $.

          1
       /     \
     2        3
   /    \     /   \
  4     5   6    7
    \
     8

Input Format:
The first line of input contains the number of test cases T. For every test case, the only line of input contains a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denote node values, and a character “N” denotes NULL child.

For example:

 
For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output Format:
For each test case, in a new line, print the output in the required format.

Your Task:
This is a function problem. You don't need to read input. Just complete the function levelOrder() that takes nodes as parameter and prints level order line-by-line. The newline for every test case is automatically appended by the driver code.

Constraints:
1 <= T<= 100
1 <= Number of edges <= 1000
1 <= Data of a node <= 100

Example:
Input:
2
1 4 N 4 2 
10 20 30 40 60 N N 
Output:
1 $ 4 $ 4 2 $
10 $ 20 30 $ 40 60 $
Explanation:
Testcase1: The tree is
                    1
                 /
               4
            /     \
         4        2
So, the level order would be 1 $ 4 $ 4 2 $
Testcase2: The tree is
                           10
                        /        \
                     20         30
                  /       \
               40       60
So, the level order would be 10 $ 20 30 $ 40 60 $'''
from collections import defaultdict



class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None
        self.map_nodes=defaultdict(Node)

    def Insert(self,parent,child,dir):
        if self.root is None:
            root_node=Node(parent)
            child_node=Node(child)
            if dir=='L':
                root_node.left=child_node
            else:
                root_node.right=child_node
            self.root=root_node

            self.map_nodes[parent]=root_node
            self.map_nodes[child]=child_node
            
            return

        parent_node = self.map_nodes[parent]
        child_node=Node(child)
        self.map_nodes[child]=child_node
        if dir=='L':
            parent_node.left=child_node
        else:
            parent_node.right=child_node
        return

    
def levelOrder(root):
    if root==None:
        return
    q=[]
    q.append(root)
    while len(q):
        levelnodes=len(q)
        while levelnodes:
            node=q[0]
            print(node.data,end=" ")
            q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            levelnodes-=1
        print('$',end=" ")
    

test_cases=int(input())    
for cases in range(test_cases):
    n=int(input())
    a=list(map(str,input().strip().split()))

    tree=Tree()
    i=0
    while i<len(a):
        parent=int(a[i])
        child=int(a[i+1])
        dir=a[i+2]
        i+=3
        tree.Insert(parent,child,dir)
    levelOrder(tree.root)
    print()
