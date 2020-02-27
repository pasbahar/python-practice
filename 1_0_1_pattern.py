'''Given a string, your task is to find the number of patterns of form 1[0]1 where [0] represents any number of zeroes (minimum requirement is one 0) there should not be any other character except 0 in the [0] sequence.

 

Input:
The first line contains T denoting the number of testcases. Then follows description of testcases. Each case contains a string.
 

Output:
For each test case, output the number of patterns.

 

Constraints:
1<=T<=20
1<=Length of String<=2000


Example:
Input:
2
100001abc101
1001ab010abc01001

 

Output:
2
2'''
for i in range(int(input())):
    s=input()
    count,lf,lf0=0,0,0
    for l in range(len(s)):
        if lf and lf0 and s[l]=='1':
            count+=1
            lf0=0
        if lf and s[l]=='0':
            lf0=1
        else:
            lf,lf0=0,0
        if s[l]=='1' and not lf:
            lf=1
    print(count)



