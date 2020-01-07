class node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None
    def insert(self,val):
        if self.head==None:
            self.head=node(val)
        else:
            new_node=node(val)
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
def createList(arr,n):
    lis=Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

def findMid(head):
    n,n1=head,head
    c=0
    while n1 and n1.next:
        n=n.next
        n1=n1.next.next
    return n

for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    head=createList(arr,n)
    print(findMid(head).data)




