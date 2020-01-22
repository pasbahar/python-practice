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