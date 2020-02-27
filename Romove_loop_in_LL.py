'''You are given a linked list of N nodes. The task is to remove the loop from the linked list, if present.

Input:
First line of input contains number of testcases T. T testcases follow. For each testcase, first line of input contains length N of the linked list and next line contains N data of the linked list. The third line contains the position of the node(from head) to which the last node will get connected. If it is 0 then there is no loop.

Output:
For each testcase, in a new line, 1 will be printed if loop is removed(correct answer) else 0 will be printed(for wrong answer).

User Task:
You don't have to read the input, or print the output. Just complete the function removeTheLoop() which has only argument as head reference of the linked list. If you complete this function in correct way and loop gets removed, the answer will be 1.

Constraints:
1 <= T <= 50
1 <= N <= 300

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
1
1

Explanation:
Testcase 1: In the first test case N = 3.
The linked list with nodes N = 3 is given. Here, x = 2 which means last node is connected with xth node of linked list. Therefore, there exists a loop. 

Testcase 2: N = 4 and x = 0, which means lastNode->next = NULL, thus the Linked list does not contains any loop.'''
def removeTheLoop(head):
    p,n=head,head
    d={}
    while n and n not in d.keys():
        d[n]=0
        p=n
        n=n.next
    p.next=None 


#{ 
#  Driver Code Starts
class Node:
    data=0
    next=None
    
    
def newNode(data):
    temp=Node()
    temp.data=data
    temp.next=None
    return temp
    
def insert(head,data):
    if(head==None):
        head=newNode(data)
    else:
        head.next=insert(head.next,data)
    return head

def makeLoop(head,x):
    if (x==0):
        return
    curr=head
    last=head
    counter=0
    while(counter<x):
        curr=curr.next
        counter+=1
    while(last.next!=None):
        last=last.next
    last.next=curr
            

def detectloop(head):
    hare=head.next
    tortoise=head
    while(hare!=tortoise and hare!=None and tortoise!=None):
        hare=hare.next
        tortoise=tortoise.next
        if(hare!=None and hare.next!=None):
            hare=hare.next
        if(hare==tortoise):
            return 1
    return 0
    
def length(head, hasloop):
    len=0
    if(hasloop==False):
        temp=head
        while(temp!=None):
            len+=1
            temp=temp.next
        return len
    else:
        hare=head.next
        tortoise=head
        while(hare!=tortoise):
            hare=hare.next
            tortoise=tortoise.next
            hare=hare.next
            if(hare==tortoise):
                break
        looplen=0
        while(hare.next!=tortoise):
            hare=hare.next
            looplen+=1
        looplen+=1
        begin=head
        startlen=0
        tortoise=tortoise.next
        while(begin!=tortoise):
            begin=begin.next
            tortoise=tortoise.next
            startlen+=1
        return looplen+startlen
        

def main():
    testcases=int(input())
    
    while(testcases>0):
        head=Node()
        head=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        x=int(input())
        
        for i in arr:
            head=insert(head,i)
        makeLoop(head,x)
        lengthll=0
        if(detectloop(head)==1):
            lengthll=length(head,True)
        else:
            lengthll=length(head,False)
        removeTheLoop(head)
        
        if(detectloop(head)==0 and lengthll==length(head,False)):
            print("1")
        else:
            print("0")
        testcases-=1

if __name__=="__main__":
    main()
# } Driver Code Ends