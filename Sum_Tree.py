'''Write a function that returns true if the given Binary Tree of size N is SumTree else return false. A SumTree is a Binary Tree in which value of each node x is equal to sum of nodes present in its left subtree and right subtree . An empty tree is SumTree and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree.

Following is an example of SumTree.

          26
        /    \
      10      3
    /   \   /   \ 
   4     6  1    2
 

Input:
The first line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denote node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
Print "1" if the given tree is SumTree else print "0".

Your Task:
You don't need to take input. Just complete the function isSumTree() that takes root node as parameter and returns true, if the tree is SumTree else returns false.
Constraints:
1 <=T<=100
1 <= N <= 103
Example:
Input:
2
3 1 2
10 20 30 10 10

Output:
1
0'''
class Node:
    def __init__(self,val):
        self.right=None
        self.data=val
        self.left=None
class Tree:
    def createNode(self,data):
        return Node(data)
    def insert(self, node, data,ch):
        if node is None:
            return self.createNode(data)
        if (ch=="L"):
            node.left=self.insert(node.left,data,ch)
            return node.left
        else:
            node.right=self.insert(node.right,data,ch)
            return node.right
    def search (self, lis, data):
        for i in lis:
            if i.data==data:
                return i

def isSumTree(head):
    if head is None:
         return 1
    if head.left and head.left.left:
        l_data=head.left.data*2
    elif head.left:
        l_data=head.left.data
    else:
        l_data=0       
    if head.right and head.right.right:
        r_data=head.right.data*2
    elif head.right:
        r_data=head.right.data
    else:
        r_data=0
    if head.data==(l_data+r_data)or (l_data+r_data)==0:
        return (1&isSumTree(head.left)&isSumTree(head.right))
    else:
        return 0


if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=input().strip().split()
        if n==0:
            print(1)
            continue
        tree=Tree()
        lis=[]
        root=None
        root=tree.insert(root,int(arr[0]),"L")
        lis.append(root)
        k=0
        for j in range(n):
            ptr=tree.search(lis,int(arr[k]))
            lis.append(tree.insert(ptr,int(arr[k+1]),arr[k+2]))
            k+=3
        if isSumTree(root):
            print(1)
        else:
            print(0)

