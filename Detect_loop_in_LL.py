'''Given a linked list of N nodes. The task is to check if the the linked list has a loop. Linked list can contain self loop.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains length of linked list and next line contains the data of linked list.

Output:
For each testcase, print "True", if linked list contains loop, else print "False".

User Task:
The task is to complete the function detectloop() which contains reference to the head as only argument. This function should return 1 if linked list contains loop, else return 0.

Constraints:
1 <= T <= 100
1 <= N <= 104
1 <= Data on Node <= 103

Example:
Input:
2
3
1 3 4
2
4
1 8 3 4
0

Output:
True
False

Explaination:
Testcase 1: In above test case N = 3. The linked list with nodes N = 3 is given. Then value of x=2 is given which means last node is connected with xth node of linked list. Therefore, there exists a loop. 

Testcase 2: For N = 4
x = 0 means then lastNode->next = NULL, then the Linked list does not contains any loop.'''
def detectLoop(head):
    #code here
    if head==None:
        return 0
    s,f=head,head
    while f.next and f.next.next:
        s=s.next
        f=f.next.next
        if f==s:
            return 1
    return 0


#{ 
#  Driver Code Starts
#Initial Template for Python 3
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

    #connects last node to node at position pos from begining.
    def add(self,pos):
        count=0
        curr_node=self.head
        temp= None

        while curr_node.next :
            count+=1
            if(count==pos):
                temp=curr_node
            curr_node=curr_node.next

        curr_node.next=temp

        return

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)
        loop = int(input())
        if(loop):
            a.add(loop)
        print(detectLoop(a.head))
# } Driver Code Ends