'''Given an array arr[] of size N. The task is to find the first repeating element in an array of integers, i.e., an element that occurs more than once and whose index of first occurrence is smallest.

Input :
The first line contains an integer T denoting the total number of test cases. In each test cases, First line is number of elements in array N and second its values.

Output:
In each separate line print the index of first repeating element, if there is not any repeating element then print “-1” (without quotes). Use 1 Based Indexing.

Constraints:
1 <= T <= 500
1 <= N <= 106
0 <= Ai <= 106

Example:
Input:
3
7
1 5 3 4 3 5 6
4
1 2 3 4
5
1 2 2 1 3

Output:
2
-1
1'''
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    d={}
    flag=0
    for i in l:
        if i  in d.keys():
            print(d[i])
            flag=1
            break
        else:
            d[i]=l.index(i)
    if not flag:
        print(-1)