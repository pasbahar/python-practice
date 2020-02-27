'''Given an array A[] of N numbers and another number x, determine whether or not there exist three elements in A[] whose sum is exactly x.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains n and x. Next line contains array elements.

Output:
Print 1 if there exist three elements in A whose sum is exactly x, else 0.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 103
1 ≤ A[i] ≤ 105

Example:
Input:
2
6 13
1 4 45 6 10 8
5 10
1 2 4 3 6

Output:
1
1

Explanation:
Testcase 1: There is one triplet with sum 13 in the array. Triplet elements are 1, 4, 8, whose sum is 13.'''
for i in range(int(input())):
    n,k=map(int,input().split())
    l=sorted(list(map(int,input().split())))
    flag=0
    for x in range(n):
        if flag==1:
            break
        lo=x+1
        r=n-1
        while(lo<r):
            if l[x]+l[lo]+l[r]<k:
                lo+=1
            elif l[x]+l[lo]+l[r]>k:
                r-=1
            else:
                flag=1
                print(1)
                break
    if not flag:
        print(0)


