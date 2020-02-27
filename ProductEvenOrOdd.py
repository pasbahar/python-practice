'''You are given two numbers N1 and N2. You need to find out if the product of these numbers generate an even number or an odd number.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test cases follow. Each test case contains two lines of input:-
The first line contains N1
The second line contains N2

Output:
For each test case, Print 1 or 0  according to the result. if even print 1 else print 0.

Constraints:
1<=T<=120
1<=N1,N2<=1099

Example:

Input:
3
5
8
2
98
773
13

Output:
1
1
0

Explanation:
For test case 1: N1 is 5, N2 is 8; 5*8=40 is even, so we print 1.'''
for i in range(int(input())):
    n1=int(input())
    n2=int(input())
    if n1%2==0 or n2%2==0:
        print(1)
    else:
        print(0)