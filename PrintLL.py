
'''You are given the pointer to the head node of a linked list. You have to print all of its elements in order in a single line.

Input:
You have to complete a method which takes one argument: the head of the linked list. You should not read any input from stdin/console. The struct Node has a data part which stores the data and a next pointer which points to the next element of the linked list. There are multiple test cases. For each test case, this method will be called individually.

Output:
Print the elements of the linked list in a single line separated by a single space.

User Task:
The task is to complete the function display() which prints the elements of the linked list.

Example:
Input:
2
2
1 2
1
4

Output:
1 2
4'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
class Linked_List:
    def __init__(self):
        self.head = None
    def get_head(self):
        return self.head
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def printlist(node):
    n=node
    while n:
        print(n.data,end=" ")
        n=n.next

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        llist = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            llist.insert(i)
        printlist(llist.get_head())
        print('')


    