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

