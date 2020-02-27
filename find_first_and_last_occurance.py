'''Given a sorted array with possibly duplicate elements. The task is to find indexes of first and last occurrences of an element X in the given array.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N denoting the size of the array. Then in the next line are N space separated values of the array. The last line of each test case contains an integer X.

Output:
For each test case in a new line print two integers separated by space denoting the first and last occurrence of the element X. If the element is not present in the array print -1.

Constraints:
1 <= T <= 100
1 <= N <= 1000
1 <= A[], X <= 1018

Example:
Input:
2
9
1 3 5 5 5 5 67 123 125
5
9
1 3 5 5 5 5 7 123 125
7

Output:
2 5
6 6'''
for i in range (int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=int(input())
    in1,in2=-1,-1
    for x in l:
        if x==k and in1==-1:
            in1=l.index(x)
        if in1!=-1 and x!=k:
            in2=l.index(x)-1
            break
    if in1!=-1 and in2==-1:
        in2=len(l)-1
    if in1==-1:
        print(-1)
    else:
        print(in1,in2)
