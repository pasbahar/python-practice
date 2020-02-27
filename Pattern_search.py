'''Given a text and a pattern. Find whether the pattern exist in the text or not. If it is present print "found" without quotes else print "not found"
without quotes.

Input:

The first line of input contains an integer T denoting the number of test cases. Each test case consist of a string in 'lowercase' only in a
separate line.

Output:

Print "found" or "not found" in a separate line.


Constraints:

1 ≤ T ≤ 30
1 ≤ |s| ≤ 100


Example:

Input
1
geeksforgeeks
geeks
Output
found'''
for i in range(int(input())):
    s1=input()
    s2=input()
    if s1.find(s2)==-1:
        print('not found')
    else:
        print('found')