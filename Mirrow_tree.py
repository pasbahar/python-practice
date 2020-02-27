'''Given a Binary Tree, convert it into its mirror.
MirrorTree1            

Input Format:

First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:


For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output Format:
For each testcase, in a new line, print inorder traversal of mirror tree.

Your Task:
You don't have to take any input. Just complete the function mirror() that takes node as paramter. The printing is done by the driver code.

Constraints:
1 <= T <= 100
1 <= Number of nodes <= 100
1 <= Data of a node <= 1000

Example:
Input:
2
1 3 2
10 20 30 40 60
Output:
2 1 3
30 10 60 20 40
Explanation:
Testcase1: The tree is
        1         (mirror)     1
     /      \         =>        /     \
   3       2                  2         3
The inorder of mirror is 2 1 3
Testcase2: The tree is
                           10                                      10
                        /        \           (mirror)         /        \
                     20         30            =>        30        20
                  /       \                                              /    \
               40       60                                        60    40
The inroder traversal of mirror is 30 10 60 20 40.'''
def mirror(root):
    # Code here
    if root==None:
        return
    root.left,root.right=root.right,root.left
    if root.left:
        mirror(root.left)
    if root.right:
        mirror(root.right)


class Node:
    def __init__(self,val):
        self.right = None
        self.data = val
        self.left = None

def inorderTraversalUtil(root):
    # Code here
    if root is None:
        return
    inorderTraversalUtil(root.left)
    print(root.data, end=' ')    
    inorderTraversalUtil(root.right)

def inorderTraversal(root):
    # Code here
    inorderTraversalUtil(root)
    print()

if __name__ == '__main__':
    t = int(input())
    
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        if n == 0:
            print(0)
            continue
        
        root = None
        dictTree = dict()
        
        for j in range(n):
            if arr[3*j] not in dictTree:
                dictTree[arr[3*j]] = Node(int(arr[3*j]))
                parent = dictTree[arr[3*j]]
                
                if j is 0:
                    root = parent
            else:
                parent = dictTree[arr[3*j]]
            
            child = Node(int(arr[3*j+1]))
                
            if(arr[3*j+2] == 'L'):
                parent.left = child
            else:
                parent.right = child
            dictTree[arr[3*j+1]] = child
                
        mirror(root)
        
        inorderTraversal(root)
# } Driver Code Ends