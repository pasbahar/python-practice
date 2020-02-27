'''Given two binary trees, the task is to find if both of them are identical or not. 

Input:

First line of input contains the number of test cases T. For each test case, there will be two lines of input each of which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:

 

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N
Output:
The function should return true if both trees are identical else false.

User task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function isIdentical() that takes two roots as parameters and returns true or false. The printing is done by the driver code.

Constraints:
1 <= T <= 100
1 <= Number of nodes <= 100
1 <=Data of a node <= 1000

Example:
Input:
3
1 2 3
1 2 3
1 2 3
1 3 2
1 2 3 N 3 N 10
1 2 3 N 3 N 10
Output
Yes
No
Yes'''
def isIdentical(root1, root2):
    if root1==None and root2==None:
        return 1
    if root1 and not root2 or root2 and not root1 or root1.data!=root2.data:
        return 0
    if root1.left==None and root1.right==None and root2.left==None and root2.right==None and root1.data==root2.data:
        return 1 
    return(isIdentical(root1.left,root2.left) and isIdentical(root1.right,root2.right))

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data, ch):
        if node is None:
            return self.createNode(data)
        if (ch == 'L'):
            node.left = self.insert(node.left, data, ch)
            return node.left
        else:
            node.right = self.insert(node.right, data, ch)
            return node.right

    def search(self, lis, data):
        # if root is None or root is the search data.
        for i in lis:
            if i.data == data:
                return i

# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        tree = Tree()
        lis=[]
        root1 = None
        root1 = tree.insert(root1, int(arr[0]), 'L')
        lis.append(root1)
        k=0
        for j in range(n):
            ptr = None
            ptr = tree.search(lis, int(arr[k]))
            lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
            k+=3
        n = int(input())
        arr = input().strip().split()
        tree = Tree()
        lis=[]
        root2 = None
        root2 = tree.insert(root2, int(arr[0]), 'L')
        lis.append(root2)
        k=0
        for j in range(n):
            ptr = None
            ptr = tree.search(lis, int(arr[k]))
            lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
            k+=3
        if isIdentical(root1, root2):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends