'''Given an string in roman no format (s)  your task is to convert it to integer .

Input:
The first line of each test case contains the no of test cases T. Then T test cases follow. Each test case contains a string s denoting the roman no.

Output:
For each test case in a new line print the integer representation of roman number s. 

Constraints:
1<=T<=100
1<=roman no range<4000

Example:
Input
2
V
III 
Output
5
3'''
def fun(s):
    c=0
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in range(len(s)):
        if i>0 and roman[s[i]]>roman[s[i-1]]:
            c+=roman[s[i]]-2*roman[s[i-1]]
        else:
            c+=roman[s[i]]
    print(c)

for i in range(int(input())):
    s=input()
    fun(s)