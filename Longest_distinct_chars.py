'''Given a string S, find length of the longest substring with all distinct characters.  For example, for input "abca", the output is 3 as "abc" is the longest substring with all distinct characters.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is String str.

Output:
Print length of smallest substring with maximum number of distinct characters.
Note: The output substring should have all distinct characters.

Constraints:
1 ≤ T ≤ 100
1 ≤ size of str ≤ 10000

Example:
Input:
2
abababcdefababcdab
geeksforgeeks

Output:
6
7'''
for i in range(int(input())):
    s=input()
    d={}
    maxlen,currlen,prevind=1,0,0
    for j in range(len(s)) and d[s[j]]>=prevind:
        if s[j] in d.keys():
            currlen=j-d[s[j]]
            prevind=d[s[j]]
            d[s[j]]=j
        else:
            d[s[j]]=j
            currlen+=1
        if maxlen<currlen:
            maxlen=currlen
    print(maxlen)
