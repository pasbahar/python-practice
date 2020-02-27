'''Azad’s mother gave him Rs. 100 so he decided to buy some chocolates, he went to a shop and that shop only has chocolates of Rs. 3 and Rs. 7 so it now depends on Azad’s mood how many chocolates he will buy. May be he will  not buy a single chocolate. Can you tell the possible remaining amount he has after coming from that shop. If N (0≤ N ≤ 100) is equal to possible remaining amount he has after he came from that shop print 1 else 0.

  For example :    Input    99

                            Output   0

Explanation :  It is not possible so output  is 0.

For example :     Input    97

                           Output   1

Explanation : 100 - (1 * 3 + 0 * 7) = 97 so output  is 1.

Input :
The first line of the input contains a single integer T denoting the number of test cases. The first line of each test case contains  N. 

Output :
For each test case, output 0 or 1. 

Constraints: 
1 ≤ T ≤ 101 
0 ≤ N ≤ 100

Example:
Input: 
4
93
97
94
99
Output: 
1
1
1
0'''
def istrue(n):
    for i in range(n//3+1):
        y=n-3*i
        if y%7==0:
            return 1
    return 0

for i in range(int(input())):
    n=int(input())
    print(istrue(100-n))