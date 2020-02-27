'''Given a Binary Tree, find diameter of it.
+The diameter of a tree is the number of nodes on the longest path between two leaves in the tree. The diagram below shows two trees each with diameter nine, the leaves that form the ends of a longest path are shaded (note that there is more than one path in each tree of length nine, but no path longer than nine nodes).



Input Format:
First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:
  
For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output Format:
For each testcase, in a new line, print the diameter.

Your Task:
You need to complete the function diameter() that takes node as parameter and returns the diameter.

Constraints:
1 <= T <= 100
1 <= Number of nodes <= 100
1 <= Data of a node <= 100

Example:
Input:
2
1 2 3
10 20 30 40 60 

Output:
3
4

Explanation:
Testcase1: The tree is
        1
     /      \
   2        3
The diameter is of 3 length.
Testcase2: The tree is
                           10
                        /        \
                     20         30
                  /       \
               40       60
The diameter is of 4 length.'''
def height(root,result):
    if root==None:
        return 0
    left=height(root.left,result)
    right=height(root.right,result)
    result[0]=max(result[0],1+left+right)
    return (1 + max(left,right))
def diameter(root):
    if root==None:
        return
    h=[0]
    height(root,h)
    return h[0]




#{ 
#  Driver Code Starts
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
        arr = list(map(str,input().strip().split()))
        if n ==0:
            print(0)
            continue
        tree = Tree()
        lis=[]
        root = None
        root = tree.insert(root, int(arr[0]), 'L')
        lis.append(root)
        k=0
        for j in range(n):
            ptr = None
            ptr = tree.search(lis, int(arr[k]))
            lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
            k+=3
        print(diameter(root))
        

# } Driver Code Ends