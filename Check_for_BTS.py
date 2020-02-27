'''Given a binary tree, return true if it is BST, else false. For example, the following tree is not BST, because 11 is in left subtree of 10. The task is to complete the function isBST() which takes one argument, root of Binary Tree.

        10
     /     \
   7       39
     \
      11

Input:
The input contains T, denoting number of testcases. For each testcase there will be two lines. The first line contains number of edges. The second line contains two nodes and a character separated by space. The first node denotes data value, second node denotes where it will be assigned to the previous node which will depend on character 'L' or 'R' i.e. the 2nd node will be assigned as left child to the 1st node if character is 'L' and so on. The first node of second line is root node. The struct or class Node has a data part which stores the data, pointer to left child and pointer to right child. There are multiple test cases. For each test case, the function will be called individually.

Output:
The function should return 1 if BST else return 0.

User Task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function isBST().

Constraints:
1 <= T <= 100
0 <= Number of edges <= 100
1 <= Data of a node <= 1000

Example:
Input:
2
2
1 2 R 1 3 L
4
10 20 L 10 30 R 20 40 L 20 60 R

Output:
0
0'''
def isBST(root):
    # Code here
    if root is None:
        return True
    if root.left:
        if root.left.data>root.data:
            return False
    if root.right:
        if root.right.data<root.data:
            return False
    if root.right and root.right.left:
        if root.right.left.data<root.data:
            return False
    if root.left and root.left.right:
        if root.left.right.data>root.data:
            return False
    return isBST(root.left) and isBST(root.right)




#{ 
#  Driver Code Starts
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:  # Binary tree Class
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

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = input().strip().split()
        if n==0:
            print(1)
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
        # tree.traverseInorder(root)
        # print ''
        if isBST(root):
            print(1)
        else:
            print(0)

# } Driver Code Ends