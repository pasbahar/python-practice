'''Given a linked list of N nodes. The task is to reverse this list.

Input: Head of following linked list
1->2->3->4->NULL
Output: Linked list should be changed to,
4->3->2->1->NULL

Input: Head of following linked list
1->2->3->4->5->NULL
Output: Linked list should be changed to,
5->4->3->2->1->NULL

Input: NULL
Output: NULL

Input: 1->NULL
Output: 1->NULL

Input:
First line of input contains number of testcases T. For each testcase, first line contains length of linked list and next line contains the elements of linked list.

Output:
Reverse the linked list and return head of the modified list.

User Task:
The task is to complete the function reverseList() which head reference as the only argument and should return new head after reversing the list.

Constraints:
1 <= T <= 100
1 <= N <= 103

Example:
Input:
2
6
1 2 3 4 5 6
5
2 7 8 9 10

Output:
6 5 4 3 2 1
10 9 8 7 2

Explanation:
Testcase 1: After reversing the list, elements are as 6->5->4->3->2->1.'''
def reverseList(self):
    # Code here
    if self.head is None:
        return None
    curr=self.head
    prev=None
    while curr:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    self.head=prev
    return self.head


# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.lastNode = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.lastNode = self.head
        else:
            new_node = node(val)
            self.lastNode.next = new_node
            self.lastNode = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    reverse_List = reverseList

    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp=tmp.next
        print()

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        lis.reverse_List()
        lis.printList()




# } Driver Code Ends