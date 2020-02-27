'''A frog jumps either 1, 2 or 3 steps to go to top. In how many ways can it reach the top.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains one line of input N denoting the total number of steps.

Output:
For each testcase, in a new line, print the number of ways to reach the top.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 50

Example:
Input:
2
1
5
Output:
1
13'''
def fib(n):
    fib1,fib2,fib3=1,1,2
    for i in range(2,n):
        fib4=fib1+fib2+fib3
        fib1=fib2
        fib2=fib3
        fib3=fib4
    if n<2:return fib1
    if n<3:return fib3
    else:return fib4

for i in range(int(input())):
    n=int(input())
    print(fib(n))