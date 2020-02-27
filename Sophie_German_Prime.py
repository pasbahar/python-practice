'''Write a program to print all sophie germain number less than n. A prime number p is called a sophie prime number if 2p+1 is also a prime number. The number 2p+1 is called a safe prime. For example 11 is a prime number and 11*2 + 1 = 23 is also a prime number so, 11 is sophie germain prime number .

Input:

The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.

 

Output: 
For each testcase, print  all sophie germain number less than n.

Constraints:

 

1<=T<=100
3<=10000<=N

Example:
Input:

1

25

Output:

2 3 5 11 23'''
def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for i in range(int(input())):
    n=int(input())
    print(2,end=" ")
    for i in range(3,n,2):
        if isprime(i) and isprime(2*i+1):
            print(i,end=' ')
    print()