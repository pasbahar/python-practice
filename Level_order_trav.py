def levelOrder( root ):
    q=[]
    q.append(root)
    while len(q):
        levelnodes=len(q)
        while levelnodes:
            temp=q[0]
            q.pop(0)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            print(temp.data,end=' ')
            levelnodes-=1

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
            
    def traverse(self, root):
        if root is not None:
            self.traverse(root.left)
            print(root.data, end=' ')
            self.traverse(root.right)

# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        tree = Tree()
        lis = {}
        root = None
        root = tree.createNode(int(arr[0]))
        lis[root.data]=root
        k=0
        for j in range(n):
            if int(arr[k]) in lis:
                ptr = tree.createNode(int(arr[k+1]))
                if arr[k+2]=='L':
                    lis[int(arr[k])].left = ptr
                else:
                    lis[int(arr[k])].right = ptr
                lis[int(arr[k+1])] = ptr
                k+=3
        levelOrder(root)
        print()