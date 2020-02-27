'''Given a number, the task is to set all odd bits of a number.

INPUT: The first line consists of an integer T i.e. the number of test cases. Each test case contains an integer n .

OUTPUT: For each test case, print the number formed after setting all the odd bits of the given number in newline.

CONSTRAINTS:

1<=T<=100
1<=n<=105

EXAMPLES:
INPUT :
2
20
10

OUTPUT : 
21
15

EXPLANATION:

Input : 20
Output : 21
Explanation : Binary representation of 20
is 10100. Setting all odd
bits make the number 10101 which is binary
representation of 21.

Input : 10
Output : 15'''
for i in range(int(input())):
    n=int(input())
    s=str(bin(n))[2:]
    l=list(s)
    for j in range(len(l)-1,0,-2):
        l[j]='1'
    s="".join(l)
    res=int(s,2)
    print(res)