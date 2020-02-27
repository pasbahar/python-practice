'''Given a number N, check if a number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number.

Input:
First line consists of T test cases. Then T test cases follow .Each test case consists of a number N.

Output:
For each testcase, in a new line, output in a single line 1 if a number is a perfect number else print 0.

Constraints:
1 <= T <= 300
1 <= N <= 1018

Example:
Input:
2
6
21
Output:
1
0'''
def perfect(n):
    sm=0
    for i in range(1,n//2+1):
        if n%i==0:
            sm+=i
    if sm==n:
        return 1
    else: return 0

for i in range(int(input())):
    n=int(input())
    print(perfect(n))



