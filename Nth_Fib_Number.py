'''Given a positive integer N, find the Nth fibonacci number. Since the answer can be very large, print the answer modulo 1000000007.

Input:
The first line of input contains T denoting the number of testcases.Then each of the T lines contains a single positive integer N.

Output:
Output the Nth fibonacci number.

Constraints:
1 <= T <= 200
1 <= N <= 1000
Example:
Input:
3
1
2
5
Output:
1
1
5'''
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        f=[]
        f.append(0)
        f.append(1)
        for i in range(2,n+1):
            f.append(f[i-1]+f[i-2])
        return f[n]%1000000007

for i in range(int(input())):
    print(fib(int(input())))