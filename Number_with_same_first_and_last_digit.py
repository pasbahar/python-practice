'''Given an range of number's starting with integer L and ending at R, the task is to count the numbers which have same first and last digits.

Input:
The first line of the input contains an integer T, denoting the number of test cases. The T test case follow. The only line of the each test case contains two space seperated integer's L and R. 

Output:
For each test case output a single line containing a single integer denoting the count of the required number's.

Constraints:
1 <= T <= 104
1 <= L,R <= 108

Example:
Input:
2
7 68
5 40
Output:
9
8

Explanation:
TestCase1:Number with same first and last digits in the given range are: [7 8 9 11 22 33 44 55 66].'''
for i in range(int(input())):
    n,k=map(int,input().split())
    c=0
    for x in range(n,k+1):
        s=str(x)
        if s[0]==s[-1]:
            c+=1
    print(c)

