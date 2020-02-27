'''Given the value of n, we need to find the sum of the series where i-th term is sum of first i odd natural numbers.

Note:- Sum of the series 1 + (1+3) + (1+3+5) + (1+3+5+7) + …… + (1+3+5+7+…+(2n-1))

Input:

The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.
Output:

Print the sum of the series of N terms for each testcase.
Constraints:

1<=T<=100

1<=N<=1000
Example:

Input:

2

2

5

Output:

5

55

Explanation:

Testcase 1:

(1) + (1+3) = 5
Testcase 2:
(1) + (1+3) + (1+3+5) + (1+3+5+7) + (1+3+5+7+9) = 55'''
for i in range(int(input())):
    n=int(input())
    res,x=0,1
    for i in range(n,0,-1):
        res=res+x*i
        x+=2
    print(res)