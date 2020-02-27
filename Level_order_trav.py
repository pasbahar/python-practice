'''You are given a tree and you need to do the level order traversal on this tree.
Level order traversal of a tree is breadth-first traversal for the tree.



Level order traversal of above tree is 1 2 3 4 5

Input:
First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
The function should print the level order traversal of the tree as specified in the problem statement.

Your Task:
You don't have to take any input. Just complete the function levelOrder() that takes node as parameter and prints the level order. The newline is automatically appended by the driver code.

Constraints:
1 <= T <= 100
1 <= Number of nodes<= 100
1 <= Data of a node <= 100

Example:
Input:
2
1 3 2
10 20 30 40 60 N N
Output:
1 3 2
10 20 30 40 60

Explanation:
Testcase1: The tree is
        1
     /      \
   3       2
So, the level order would be 1 3 2
Testcase2: The tree is
                           10
                        /        \
                     20         30
                  /       \
               40       60
So, the level order would be 10 20 30 40 60'''
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