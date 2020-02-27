'''Given a binary tree, connect the nodes that are at same level.
Structure of the given Binary Tree node is like following.

struct Node
{
      int data;
      Node* left;
      Node* right;
      Node* nextRight;
}
Initially, all the nextRight pointers point to garbage values. Your function should set these pointers to point next right for each node.
       10                       10 ------> NULL
      / \                       /      \
     3   5       =>     3 ------> 5 --------> NULL
    / \     \               /  \           \
   4   1   2          4 --> 1 -----> 2 -------> NULL

Input Format:
First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output Format:
For each testcase, in a new line, print the level order and inorder traversals.

Your Task:
You don't have to take input. Complete the function connect() that takes node as parameter and connects the nodes at same level. The printing is done by the driver code.

Constraints:
1 <= T <= 100
1 <= Number of nodes <= 100
1 <= Data of a node <= 1000

Example:
Input:
2
3 1 2
10 20 30 40 60
Output:
3 1 2
1 3 2
10 20 30 40 60
40 20 60 10 30

Explanation:
Testcase1: The connected tree is
        3 ------> NULL
     /      \
   1 -----> 2 ------ NULL
Testcase2: The connected tree is
                           10 ----------> NULL
                        /        \
                     20 ------> 30 -------> NULL
                  /       \'''
def connect(root):
    if root is None:
        return
    q=[]
    q.append(root)
    while len(q):
        levelnodes=len(q)
        while levelnodes:
            temp=q[0]
            q.pop(0)
            if levelnodes!=1:
                temp.nextRight=q[0]
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            levelnodes-=1

from collections import defaultdict # default dict used as a map, to store node-value mapping.


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        self.nextRight = None

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

def InOrder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated in order Traversal of the given tree.
    '''
    if root is None: # check if the root is none
        return
    InOrder(root.left) # do in order of left child
    print(root.data, end=" ")  # print root of the given tree
    InOrder(root.right) # do in order of right child

def printSpecial(root):
    leftmost_node = root

    while leftmost_node :
        curr_node = leftmost_node
        leftmost_node = None
        if curr_node.left :
            leftmost_node = curr_node.left
        elif curr_node.right :
            leftmost_node = curr_node.right

        print(curr_node.data,end=" ")
        while curr_node.nextRight :
            print(curr_node.nextRight.data,end=" ")
            curr_node = curr_node.nextRight
    print()

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
        connect(tree.root)
        printSpecial(tree.root)
        InOrder(tree.root)
        print()

