'''Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    /    \
  4     5   6    7
   \
     8   

Input:
The first line of input contains the number of test cases T. For every test case, the first line of input contains two space-separated integers, denoting node values for which we want to find LCA,  and the second line will contain a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denote node values, and a character “N” denotes NULL child.

For example:

 
For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
The function should print nodes in left view of Binary Tree.

User Task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function leftView() that prints the left view. The newline is automatically appended by the driver code.

Constraints:
1 <= T <= 100
1 <= Number of nodes <= 100
1 <= Data of a node <= 1000

Example:
Input:
2
1 3 2
10 20 30 40 60 N N
Output:
1 3
10 20 40

Explanation:
Testcase 2: below is a given tree with its nodes.

We can clearly see that nodes which are at left view of tree they are 10 20 40.'''
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