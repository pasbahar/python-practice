'''Given a positive integer N, calculate the sum of all prime numbers between 1 and N(inclusive).

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains one line of input containing N.

Output:
For each testcase, in a new line, print the sum of all prime numbers between 1 and N.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106

Example:
Input:
2
5
10
Output:
10
17'''
def sumofprime(n):
    prime=[True for j in range(n+1)]
    for p in range(2,int(n**0.5)+1):
        if prime[p]==True:
            for j in range(p*2,n+1,p):
                prime[j]=False
    sum=0
    for j in range(2,n+1):
        if prime[j]:
            sum+=j
    return sum

for i in range(int(input())):
    n=int(input())
    print(sumofprime(n))

