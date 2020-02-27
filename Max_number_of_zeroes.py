'''Given an array of N values. Print the number which has maximum number of zeroes. If there are no zeroes then print -1.

Note: If there are multiple numbers with same (max) number of zeroes then print the Maximum number among them.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains two lines of input. The first line consists of an integer N. The next line consists of N spaced integers.

Output:
For each testcase, print the number with maximum number of zeroes.

Constraints: 
1<=T<=100
1<=N<=107
1<=A[i]<=10100

Example:
Input:
1
5
10 20 3000 9999 200
Output:
3000

Explanation:
Testcase1: 3000 hsa maximum number of zeroes so we print it.'''
for i in range(int(input())):
    n=int(input())
    l=list(map(str,input().split()))
    max_c=0
    res='-1'
    for x in l:
        count=0
        for j in x:
            if j=='0':
                count+=1
        if max_c<count:
            max_c=count
            res=x
        elif max_c==count and max_c!=0:
            if int(x)>int(res):
                res=x
    print(res)



