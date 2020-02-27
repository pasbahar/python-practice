'''Given a string S consisting of lowercase Latin Letters. Find the first non repeating character in S.

Input:
The first line contains T denoting the number of testcases. Then follows description of testcases.
Each case begins with a single integer N denoting the length of string. The next line contains the string S.

Output:
For each testcase, print the first non repeating character present in string. Print -1 if there is no non repeating character.

Constraints:
1 <= T <= 900
1 <= N <= 104

Example:
Input :
3
5  
hello
12
zxvczbtxyzvy
6
xxyyzz

Output :
h
c
-1'''
for i in range(int(input())):
    n=int(input())
    s=input()
    d={}
    flag=0
    for x in s:
        if x in d:
            d[x]+=1
        else:
            d[x]=1
    for x in s:
        if d[x]==1:
            print(x)
            flag=1
    if not flag:
        print(-1)
