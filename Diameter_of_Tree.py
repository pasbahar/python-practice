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