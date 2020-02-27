'''Given an array A of positive integers. Push all the zero’s of a given array to the end of the array.

Input:
The first line contains an integer T denoting the total number of test cases. In each test cases, first line is number of elements in array N and next line contains array elements.

Output:
Print the array after shifting all 0's at the end.​

Constraints:
1 <= T <= 100
1 <= N <= 103
0 <= Ai <=103

Example:
Input:
1
5
3 5 0 0 4

Output:
3 5 4 0 0'''
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for x in l:
        if x==0:
            l.remove(x)
            l.append(0)
    print(*l)