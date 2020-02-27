'''Given a collection of Intervals,merge all the overlapping Intervals.
For example:

Given [1,3], [2,6], [8,10], [15,18],

return [1,6], [8,10], [15,18].

Make sure the returned intervals are sorted.

 

Input:

The first line contains an integer T, depicting total number of test cases. 
Then following T lines contains an integer N depicting the number of Intervals and next line followed by the intervals starting and ending positions 'x' and 'y' respectively.


Output:

Print the intervals after overlapping in sorted manner.  There should be a newline at the end of output of every test case.

Constraints:

1 ≤ T ≤ 50
1 ≤ N ≤ 100
0 ≤ x ≤ y ≤ 100


Example:

Input
2
4
1 3 2 4 6 8 9 10
4
6 8 1 9 2 4 4 7

Output
1 4 6 8 9 10
1 9'''
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    arr,res=[],[]
    for i in range(0,2*n,2):
        arr.append([l[i],l[i+1]])
    arr.sort(key=lambda x:x[0])
    temp=arr[0][1]
    res.append([arr[0][0],arr[0][1]])
    for i in range(1,n):
        if arr[i][0]>temp:
            temp=arr[i][1]
            res.append([arr[i][0],arr[i][1]])
        elif res[-1][1]<arr[i][1]:
            res[-1][1]=arr[i][1]
    for i in range(len(res)):
        print(res[i][0],res[i][1],end=" ")
    print()


