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