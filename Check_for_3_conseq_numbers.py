'''Given an integer n, the task is to find whether n can be written as sum of three consecutive integer.

Input:

The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.


Output:

For each testcase, if it is possible to write as a sum of three consecutive integers  then print three consecutive integer, else print “-1”.
Constraints:

1<=T<=100

1<=N<=10000
Example:

Input:

2

6

7

Output:

1 2 3

-1'''
for i in range(int(input())):
    n=int(input())
    if n%3==0:
        print(n//3-1," ",n//3," ",n//3+1)
    else:
        print(-1)