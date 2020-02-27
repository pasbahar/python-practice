'''Given a string without spaces, a character, and a count, the task is to print the string after the specified character has occurred count number of times.
Print “Empty string” incase of any unsatisfying conditions.
(Given character is not present, or present but less than given count, or given count completes on last index).
If given count is 0, then given character doesn’t matter, just print the whole string.

 

Input:

First line consists of T test cases. First line of every test case consists of String S.Second line of every test case consists of a character.Third line of every test case consists of an integer.


Output:

Single line output, print the remaining string or "Empty string".


Constraints:

1<=T<=200
1<=|String|<=10000


Example:

Input:

2
Thisisdemostring
i    
3​
geeksforgeeks
e
2

Output:
ng
ksforgeeks'''
for i in range(int(input())):
    s=input()
    ch=input()
    c=int(input())
    count,ind=0,-1
    for j in range(len(s)):
        if s[j]==ch:
            count+=1
        if count==c:
            ind=j+1
            break
    if c==0:
        print(s)
    elif ind!=-1 and ind!=len(s):
        s=list(s)
        s=s[ind:]
        s=''.join(s)
        print(s)
    else:
        print('Empty string')