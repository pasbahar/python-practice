'''Given N activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

Note : The start time and end time of two activities may coincide.

Input:
The first line contains T denoting the number of testcases. Then follows description of testcases. First line is N number of activities then second line contains N numbers which are starting time of activies.Third line contains N finishing time of activities.

Output:
For each test case, output a single number denoting maximum activites which can be performed in new line.

Constraints:
1<=T<=50
1<=N<=1000
1<=A[i]<=100

Example:
Input:
2
6
1 3 2 5 8 5
2 4 6 7 9 9
4
1 3 2 5
2 4 3 6

Output:
4
4'''
import operator
for i in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    f=list(map(int,input().split()))
    d=[]
    count=1
    for x in range(n):
        d.append((s[x],f[x]))
    d.sort(key=operator.itemgetter(1))
    l=0
    for j in range(1,n):
        if d[l][1]<=d[j][0]:
            l=j
            count+=1
    print(count)
    