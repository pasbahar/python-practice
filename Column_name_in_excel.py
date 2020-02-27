'''Given a positive integer, return its corresponding column title as appear in an Excel sheet.
MS Excel columns has a pattern like A, B, C, … ,Z, AA, AB, AC,…. ,AZ, BA, BB, … ZZ, AAA, AAB ….. etc. In other words, column 1 is named as “A”, column 2 as “B”, column 27 as “AA”.

Input:
The first line of each input consists of the test cases. And, the second line consists of a number N.

Output:
In each separate line print the corresonding column title as it appears in an Excel sheet.

Constraints:
1 ≤ T ≤ 70
1 ≤ N ≤ 4294967295

Example:
Input:
2
28
13
Output:
AB
M'''
def colname(n):
    temp=n
    res=[]
    rem,carry=0,0
    while(temp):
        rem=temp%26
        if not rem:
            rem=26
        temp=(temp-1)//26
        res.append(chr(int(ord('A')-1+rem)))
    return res

for i in range(int(input())):
    n=int(input())
    arr=colname(n)
    for i in arr[::-1]:
        print(i,end="")
    print()