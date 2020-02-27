'''In a native language the increasing order of priority of characters is a, b, c, d, e, f, g, h, i, j, k, l, m, n, ’ng’ , o, p, q, r, s, t, u, v, w, x, y, z. You are given two strings string1 and string2 and your task is to compare them on the basis of the given priority order.

Print ‘0’ if both the strings are equal, ‘1’ if string1 is greater than string2 and ‘-1’ if string1 is lesser than string2. All the strings consist of lowercase English alphabets only.

 

Input:

The first line of the input contains a single integer T denoting the number of test cases. Each of the test case consists of a single line containing space separated two strings string1 and string2.
 

Output:

For each test case, print the required output in a new line.
 

Constraints:

1 <= T <= 1000

1 <= |string1, string2| <= 10^8
 

Example:

Input:

3

adding addio

abcng abcno

abngc abngc

Output:

-1

1

0

Explanation:

Assume 0-based indexing.

For the 1st test case:

The Strings differ at index = 4. Comparing ‘ng’ and ‘o’, we have string1 < string2.

For the 2nd test case:

The Strings differ at index = 3. Comparing ‘ng’ and ‘n’, we have string1 > string2.

For the 3rd test case:

Both the strings are same.'''
def compare(s1,s2):
    if s1==s2:
        return 0
    elif s1.find('ng')!=-1 or s2.find!=-1:
        s1=s1.replace('ng','N')
        s2=s2.replace('ng','N')
        x=0
        while x<len(s1)and x<len(s2):
            if s1[x]!=s2[x]:
                if s1[x]=='N':
                    if s2[x]<='n':
                        return 1
                    else:
                        return -1
                if s2[x]=='N':
                    if s1[x]<='n':
                        return -1
                    else:
                        return 1
            if s1[x]>s2[x]:
                return 1
            if s1[x]<s2[x]:
                return -1
            x+=1
        if len(s1)>len(s2):
            return 1
        else:
            return -1
    else:
        if s1<s2:
            return -1
        elif s1>s2:
            return 1

       
for i in range(int(input())):
    s1,s2=map(str,input().split())
    print(compare(s1,s2))