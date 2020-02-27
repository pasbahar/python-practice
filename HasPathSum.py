'''Given a Binary Tree and a sum s, your task is to check whether there is a root to leaf path in that tree with the following sum . You are required to complete the function hasPathSum. You should not read any input from stdin/console. There are multiple test cases. For each test case, this method will be called individually.

Input:
The task is to complete the function hasPathSum which takes 2 arguments, root of the Tree and a value sum. The struct node has a data part which stores the data, pointer to left child and pointer to right child.
There are multiple test cases. For each test case, this method will be called individually.

Output:
The function should return the true if such path exist else return false.

Constraints:
1 <=T<= 30
1 <=Number of nodes<= 100
1 <=Data of a node<= 1000

Example:

Input
2
2
1 2 L 1 3 R
2 
2
1 2 L 1 3 R
4

Output 
0
1

In above example there are two   test case where each represents a  tree with 3 nodes and 2 edges where root is 1, left child of 1 is 2 and right child of 1 is 3.  

'''
def hasPathSum(root,sm):
    if not root:
        return sm==0
    else:
        res=False
        subsum=sm-root.data
        if subsum==0 and not root.right and not root.left:
            return True
        if root.left:
            res=hasPathSum(root.left,subsum) or res
        if root.right:
            res=hasPathSum(root.right,subsum) or res
        return res


#contributed by RavinderSinghPB
from collections import defaultdict
class root:
    def __init__(self,val=None):
        self.data=val
        self.left=None
        self.right=None
        
# Tree Class
class Tree:
    def __init__(self):
        self.root = None
        self.map_roots = defaultdict(root)
    def Insert(self,parent, child,dir):
        if self.root is None:
            root_root = root(parent)
            child_root = root(child)
            if dir == 'L':
                root_root.left = child_root
            else:
                root_root.right = child_root
            self.root = root_root
            self.map_roots[parent] = root_root
            self.map_roots[child] = child_root
            return
        parent_root = self.map_roots[parent]
        child_root = root(child)
        self.map_roots[child] = child_root
        if dir == 'L':
            parent_root.left = child_root
        else:
            parent_root.right = child_root
        return
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of roots in tree
        a = list(map(str, input().strip().split()))  # parent child info in list

        # construct the tree according to given list
        tree = Tree()
        i = 0
        while (i < len(a)):
            parent = int(a[i])
            child = int(a[i + 1])
            dir = a[i + 2]
            i += 3
            tree.Insert(parent, child, dir)  # Insert the roots in tree.
        target=int(input())
        ans=hasPathSum(tree.root, target)
        if ans:
            print(1)
        else:
            print(0)
# } Driver Code Ends