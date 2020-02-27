'''Given a positive integer n, find if it can be expressed as xy where y > 1 and x > 0 and x and y both are both integers.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow . Each test cases contains an integer N.

Output:
For each test case in a new line print 1 if the number can be expressed as  xy else print 0.

Constraints:
1<=T<=1000
1<=n<=100

Example:
Input:
2
8
5
Output:
1
0'''
def ispower(n):
    flag=False
    for i in range(2,int(n**0.5)+1):
        p=n
        while(1):
            if p==1:
                flag=True
                break
            elif p%i==0:
                p/=i
            else:
                break
    if (flag or n==1):
        print(1)
    else:
        print(0)

for i in range(int(input())):
    n=int(input())
    ispower(n)
            