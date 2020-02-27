'''Given a singly linked list of size N of integers. The task is to check if the given linked list is palindrome or not.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains length of linked list N and next line contains N integers as data of linked list.

Output:
For each test case output will be 1 if the linked list is a palindrome else 0.

User Task:
The task is to complete the function isPalindrome() which takes head as reference as the only parameter and returns true or false if linked list is palindrome or not respectively.

Constraints:
1 <= T <= 103
1 <= N <= 50

Example(To be used only for expected output):
Input:
2
3
1 2 1
4
1 2 3 4

Output:
1
0

Explanation:
Testcase 1: 1 2 1, linked list is palindrome.'''
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
# returns the size of linked list

def is_palindrome(l):
    ll = len(l)
    if ll == 0:
        return 1
    elif ll == 1:
        return 1
    elif l[0] == l[-1]:
        return is_palindrome(l[1:-1])
    else:
        return 0
    

def isPalindrome(head):
    cb = []
    while head:
        cb.append(head.data)
        head = head.next
    return is_palindrome(cb)

t=int(input())
for cases in range(t):
    n = int(input())
    a = LinkedList() # create a new linked list 'a'.
    nodes_a = list(map(int, input().strip().split()))
    for x in nodes_a:
        a.append(x)  # add to the end of the list
    if isPalindrome(a.head):
        print(1)
    else:
        print(0)


