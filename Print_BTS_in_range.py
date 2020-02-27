'''Given a Binary Search Tree (BST) and a range, print all the numbers in the BST that lie in the given range l-h(inclusive) in non-decreasing order. If no such element exists, an empty line will be printed.
Note: Element greater than or equal to root go to the right side.

Input Format:
The first line of the input contains an integer 'T' denoting the nummber of test cases. Then 'T' test cases follow. Each test case consists of three lines. Description of  test cases is as follows:
The First line of each test case contains an integer 'N' which denotes the number of nodes in the BST.   .
The Second line of each test case contains 'N' space separated values of the nodes in the BST.
The Third line of each test case contains two space separated integers 'l' and 'h' denoting the range.

Output Format:
For each testcase, in a new line, print print all the numbers in the BST that lie in the given range in non-decreasing order.

Your Task:
This is a function problem. You don't have to take any input. Complete the function printNearNodes() that takes root, l, h as parameters and prints numbers in the BST that lie in the given range in non-decreasing order.

Constraints:
1 <= T <= 100
1 <= N <= 50
1 <= l < h < 1000

Example:
Input:
2
6
10 5 50 1 40 100
5 45
4
5 6 3 2
1 4

Output:
5 10 40
2 3

Explanation:
Testcase 1: Elements which are in the range of 5 and 45(inclusive) are 5 10 40.'''
def printNearNodes(root,l,h):
    if root==None:
        return
    if root.left:
        printNearNodes(root.left,l,h)
    if root.data>=l and root.data<=h:
        print(root.data,end=" ")
    if root.right:
        printNearNodes(root.right,l,h)


class Node:
    def __init__(self, var):
        self.data = var
        self.left = None
        self.right = None
    

def createNewNode(value):
    temp=Node(value)
    temp.data=value
    temp.left=None
    temp.right=None
    return temp
    

def newNode(root,data):
    if(root is None):
        root=createNewNode(data)
    elif(data<root.data):
        root.left=newNode(root.left,data);
    else:
        root.right=newNode(root.right,data)
        
    return root


def main():
    testcases=int(input())
    while(testcases>0):
        root=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        for i in arr:
            root=newNode(root,i)
            
        lh=[int(x) for x in input().strip().split()]
        
        printNearNodes(root,lh[0],lh[1])
        print()
        
        testcases-=1

if __name__=="__main__":
    main()


# } Driver Code Ends