'''Given a string containing multiple words, your task is to count the characters in each word and display them.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each testcase contains a string as input.

Output:
For each testcase, print the number of characters in each word of the string.

Constraints:
1<=T<=100

Example:

Input:
2
the quick brown fox
geeks for geeks

Output:
3 5 5 3
5 3 5

Explanation:
For testcase 1:
the has 3 characters
quick has 5 characters
brown has 5 characters
fox has 3 characters'''
for i in range(int(input())):
    l=list(input().split())
    res=[]
    for x in l:
        res.append(len(x))
    print(*res)