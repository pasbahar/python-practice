'''Given an array. The task is to arrange the array such that odd elements occupy the odd positions and even elements occupy the even positions. The order of elements must remain same. Consider zero-based indexing. After printing according to conditions, if remaining, print the remaining elements as it is.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, in a new line print the arranged array.

Constraints:
1<=T<=100
1<=N<=105
1<=A[i]<=105

Example:
Input:
2
6
1 2 3 4 5 6
4
3 2 4 1
Output:
2 1 4 3 6 5
2 3 4 1'''
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    res=[0 for x in range(n)]
    even,odd,j=0,1,0
    while(even<n and odd<n):
        if l[j]%2==0:
            res[even]=l[j]
            even+=2
        else:
            res[odd]=l[j]
            odd+=2
        j+=1
    while(even<n):
        res[even]=l[j]
        even+=2
        j+=1
    while(odd<n):
        res[odd]=l[j]
        odd+=2
        j+=1
    print(*res)

