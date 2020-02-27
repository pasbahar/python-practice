'''Given an array in such a way that the elements stored in array are in increasing order initially and then after reaching to a peak element , elements stored are in decreasing order. Find the highest element.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case consists of an integer n. The next line consists of n spaced integers. 

Output:
Print the highest number in the array.

Constraints: 
1<=T<=100
1<=n<=200
1<=a[i]<=105

Example:
Input:
2
11
1 2 3 4 5 6 5 4 3 2 1
5
1 2 3 4 5 

Output:
6
5'''
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    low,high=0,n-1
    if n==1:
        print(l[0])
    elif l[0]>l[1]:
        print(l[0])
    elif l[n-1]>l[n-2]:
        print(l[n-1])
    else:
        while(low<=high):
            mid=(high+low)//2
            if l[mid]>l[mid-1] and l[mid]>l[mid+1]:
                print(l[mid])
                break
            elif l[mid]>l[mid-1]:
                low=mid+1
            else:
                high=mid-1
    