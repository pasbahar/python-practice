'''Given an array containing N words consisting of lowercase characters. Your task is to find the most frequent word in the array. If multiple words have same frequency, then print the word whose first occurence occurs last in the array as compared to the other strings with same frequency.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each test case contains 2 lines, the size of array N and N words separated by spaces.

Output:
For each testcase, output the most frequent word.

Constraints:
1 <= T <= 100
1 <= N <= 1000

Example:
Input:
3
3
geeks for geeks
2
hello world
3
world wide fund

Output:
geeks
world
fund'''
for i in range(int(input())):
    n=int(input())
    l=list(input().split())
    d1={}
    d2={}
    most,last=1,-1
    for x in l:
        if x in d1.keys():
            d1[x]+=1
        else:
            d1[x]=1
            d2[x]=l.index(x)
        if d1[x]>=most:
            most=d1[x]
    for x in d1.keys():
        if d1[x]==most and d2[x]>last:
            res=x
            last=d2[x]
    print(res)
