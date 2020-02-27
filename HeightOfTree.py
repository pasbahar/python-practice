

'''Given a binary tree, find height of it.

        1
     /     \
   10      39
  /
5
The above tree has a height of 3.
Note: Height of empty tree is considered 0.

Input Format:
First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denote node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output Format:
For each testcase, in a new line, print the height of tree.

Your Task:
You don't have to take input. Complete the function height() that takes node as parameter and returns the height. The printing is done by the driver code.

Constraints:
1 <= T <= 100
1 <= Number of nodes <= 105
1 <= Data of a node <= 105
Sum of N over all testcases doesn't exceed 105

Example:
Input:
3
1 2 3
2 N 1 3 N
10 20 30 40 60 N N
Output:
2
3
3
Explanation:
Testcase1: The tree is
        1
     /      \
   2        3
So, the height would be 2.
Testcase2: The tree is
                           2
                              \
                               1 
                              /    
                          3
So, height would be 3.
Testcase3: The tree is

                           10
                        /        \
                     20         30
                  /       \
               40       60

So, height would be 3.'''

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

def height(root):
    if root==None:
         return 0
    a=height(root.left)
    b=height(root.right)
    if a>b:
        return a+1
    return b+1


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
    print(height(tree.root))




