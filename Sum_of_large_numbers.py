'''Given two non-negative numbers X and Y. The task is calculate the sum of X and Y. If the number of digits in sum (X+Y) are equal to the number of digits in X, then print sum, else print X.

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two numbers X and Y.

Output:
For each test case, print the required answer.

Constraints:
1<=T<=500
1<=|Digits in X,Y|<=100

Example:
Input:
2
25 23
100 1000

Output:
48
100

EXPLANATION:

TestCase2: Since 100+1000=1100 which has 4 digits while 100(i.e X) has only 3 digits.Hence our answer will be 100 as per the prob statement.'''
for i in range(int(input())):
    n1,n2=map(int,input().split())
    res=str(n1+n2)
    if len(res)==len(str(n1)):
        print(res)
    else:
        print(n1)
