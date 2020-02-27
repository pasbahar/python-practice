'''You are given a number N. Your task is to determine if N is an amazing number or not.  A number is called amazing if it has exactly three distinct divisors.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each testcase contains a single line having N as input.

Output:
For each testcase, print 1 if the number is amazing, else print 0.

Constraints:
1<=T<=1112
2<=N<=1018

Example:

Input:
3
2
3
4

Output:
0
0
1

Explanation:

For testcase 1: 2 has the following divisors: 1, 2. Only 2 divisors, so we print 0.
For testcase 2: 3 has the following divisors: 1, 3. Only 2 divisors, so we print 0.
For testcase 3: 4 has the following divisors: 1, 2,4. Exactly 3 divisors, so we print 1.'''
def isprime(n):
    for i in range(2,int(n**0.5)+1,1):
        if n%i==0:
            return False
    return True

for i in range(int(input())):
    n=int(input())
    temp=n**0.5
    flag=0
    if int(temp)==temp:
        if isprime(temp):
            print(1)
            flag=1
    if not flag:
        print(0)
