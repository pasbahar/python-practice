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


