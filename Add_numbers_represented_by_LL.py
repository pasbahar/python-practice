'''Given two numbers represented by two linked lists of size N and M. The task is to return a sum list. The sum list which is a linked list representation of addition of two input numbers.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains length of first linked list and next line contains N elements of the linked list. Again, next line contains M, and following line contains M elements of the linked list.

Output:
Output the resultant linked list.

User Task:
The task is to complete the function addTwoLists() which has node reference of both the linked lists and returns the head of new list.

Constraints:
1 <= T <= 100
1 <= N, M <= 100

Example:
Input:
2
2
4 5
3
3 4 5
2
6 3
1
7

Output:
0 9 3 
0 7

Explaination:
5->4 // linked list repsentation of 45.
5->4->3 // linked list representation of 345.
0->9 ->3 // linked list representation of 390 resultant linked list.'''
def addBoth(head_a,head_b):
    s1,s2=str(),str()
    p1,p2=head_a,head_b
    while p1:
        s1+=str(p1.data)
        p1=p1.next
    while p2:
        s2+=str(p2.data)
        p2=p2.next
    sum=int(s1[::-1])+int(s2[::-1])
    sumstr=str(sum)
    sumstr=sumstr[::-1]
    res=LinkedList()
    for i in sumstr:
        res.append(int(i))
    return res.head



# Node Class
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

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n_a = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_a = nodes_a[::-1] # reverse the input array
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        n_b =int(input())
        b = LinkedList()  # create a new linked list 'b'.
        nodes_b = list(map(int, input().strip().split()))
        nodes_b = nodes_b[::-1]  # reverse the input array
        for x in nodes_b:
            b.append(x)  # add to the end of the list

        result_head = addBoth(a.head,b.head)
        printList(result_head)
# } Driver Code Ends