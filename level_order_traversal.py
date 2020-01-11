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
