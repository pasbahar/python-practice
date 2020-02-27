'''Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

Input:
The first line contains T, denoting the number of testcases. Then follows description of testcases. Each case begins with a single positive integer N denoting the size of array. The second line contains the N space separated positive integers denoting the elements of array A.

Output:
For each testcase, print "Yes" or  "No" whether it is Pythagorean Triplet or not (without quotes).

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= A[i] <= 1000

Example:
Input:
1
5
3 2 4 6 5

Output:
Yes'''
for i in range(int(input())):
    n=int(input())
    arr=sorted(list(map(int,input().split())))

    for r in range(n):
        arr[r]=arr[r]*arr[r]
    flag=0
    for j in range(n-1,1,-1):
        l=0
        r=j-1
        if flag:
            break
        while(l<r):
            if arr[l]+arr[r]==arr[j]:
                flag=1
                break
            elif arr[r]+arr[l]<arr[j]:
                l+=1
            else:
                r-=1
    if flag:
        print("YES")
    else:
        print("NO")

