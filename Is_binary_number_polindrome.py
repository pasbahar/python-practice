'''Given a non-negative integer N. The problem is to check if binary representation of n is palindrome or not. Note that the actual binary representation of the number is being considered for palindrome checking, no leading 0’s are being considered.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each test case contains a single line of input denoting the number N.

Output:
For each test case, print 1 if binary representation of N is palindrome; else print 0.

Constraints:
1<=T<=200
0<=N<=263-1

Example:

Input:
3
1
2
3

Output:
1
0
1'''
for i in range(int(input())):
    s=bin(int(input()))
    l=list(s)
    l=l[2:]
    if l==l[::-1]:
        print(1)
    else:
        print(0)


