def LeftView(root):
    if root==None:
        return
    q=[]
    q.append(root)
    while len(q):
        levelnodes,newlevel=len(q),len(q)
        while levelnodes:
            temp=q[0]
            q.pop(0)
            if newlevel==levelnodes:
                print(temp.data,end=" ")
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            levelnodes-=1

from collections import defaultdict # default dict used as a map, to store node-value mapping.


# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

# Tree Class
class Tree:
    def __init__(self):
        self.root = None
        self.map_nodes = defaultdict(Node)

    def Insert(self,parent, child,dir):
        if self.root is None:
            root_node = Node(parent)
            child_node = Node(child)
            if dir == 'L':
                root_node.left = child_node
            else:
                root_node.right = child_node
            self.root = root_node

            self.map_nodes[parent] = root_node
            self.map_nodes[child] = child_node

            return

        parent_node = self.map_nodes[parent]
        child_node = Node(child)
        self.map_nodes[child] = child_node

        if dir == 'L':
            parent_node.left = child_node
        else:
            parent_node.right = child_node

        return

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(str, input().strip().split()))  # parent child info in list

        # construct the tree according to given list
        tree = Tree()
        i = 0
        while (i < len(a)):
            parent = int(a[i])
            child = int(a[i + 1])
            dir = a[i + 2]
            i += 3
            tree.Insert(parent, child, dir)  # Insert the nodes in tree.
        LeftView(tree.root)
        print()
# } Driver Code Ends