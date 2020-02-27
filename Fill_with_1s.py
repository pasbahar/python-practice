'''Given an array of 0 and 1. In how many iterations it is possible that the whole array can be filled with 1's, if in a single iteration immediate neighbours of 1's can be filled.

Input:
The first line contains a single integer T, the number of test cases. The first line consists of a single integer N(length of array). The next line consists of a N spaced integers(either 0 or 1).

Output:
For each testcase, print the minimum number of iterations to fill the whole array with 1's (if possible). If it is not possible to fill the array with 1s, print "-1" (without quotes).

Constraints:
1 <= T <= 103
1 <= N <= 107
0 <= Ai <= 1

Examples:
Input:
2
4
1 0 1 0
17
0 0 1 1 0 0 1 1 0 1 1 1 1 0 0 0 1
Output:
1
2

Explanation:
Test Case 1: Both the 0s has 1 as their immediate neighbour. So, we only need one iteration to fill the array with 1.'''
import math
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    flag,count,max_count,s=0,0,0,0
    if not l[0]:
        try:
            count=l.index(1)
            max_count=count
        except:
            flag=1
            print(-1)
    if not flag:
        for i in range(1,n-1):
            if l[i]:
                count=i-1-s
                s=i
            if max_count<math.ceil(count/2):
                max_count=math.ceil(count/2)
    count=n-1-s
    if not l[-1]:
        count=n-1-s
        if max_count<count:
            max_count=count
    elif l[-1]:
        count=n-1-1-s
        if max_count<math.ceil(count/2):
            max_count=math.ceil(count/2)
    if not flag:
        print(max_count)

