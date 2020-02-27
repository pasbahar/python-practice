'''Given a linked list consisting of L nodes and given a number N. The task is to find the Nth node from the end of the linked list.

Input:
First line of input contains number of testcase T. For each testcase, first line of input contains number of nodes in the linked list and the number N. Next line contains N nodes of linked list.

Output:
For each testcase, output the data of node which is at Nth distance from end.

User Task:
The task is to complete the function getNthFromLast() which takes two arguments: reference to head and N and you need to return Nth from end.

Constraints:
1 <= T <= 200
1 <= L <= 103
1 <= N <= 103

Example:
Input:
2
9 2
1 2 3 4 5 6 7 8 9
4 5
10 5 100 5

Output:
8
-1

Explanation:
Testcase 1: In the first example, there are 9 nodes in linked list and we need to find 2nd node from end.  2nd node from end os 8.  
Testcase 2: In the second example, there are 4 nodes in linked list and we need to find 5th from end.  Since 'n' is more than number of nodes in linked list, output is -1.'''
def getNthfromEnd(head,nth):
    p1=head
    c=0
    if head==None:
        return -1;
    if nth>n:
        return -1
    while p1:
        if c==n-nth:
            return p1.data
        p1=p1.next
        c+=1



class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n,nth_node = map(int, input().strip().split())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        print(getNthfromEnd(a.head,nth_node))
# } Driver Code Ends