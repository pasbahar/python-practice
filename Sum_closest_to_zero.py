'''Given an integer array A of N elements. You need to find the sum of two elements such that sum is closest to zero.

Input:
The first line of input contains an integer T denoting the number of test cases.  
The first line of each test case is N, denoting the size of array. Each test case consist of a N integers which are the array elements.

Output:
Print the requiired sum which is closest to zero.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 103
-106 ≤ a[i] ≤ 106

Example:
Input:
3
3
-8 -66 -60  
6
-21 -67 -37 -18 4 -65  
2
-24 -73

Output:
-68
-14
-97'''
for i in range(int(input())):
    n=int(input())
    arr=sorted(list(map(int,input().split())))
    minsumpos=9999999
    minsumneg=-9999999
    l,r=0,n-1
    while(l<r):
        temp=arr[l]+arr[r]
        if temp>0:
            if minsumpos>temp:
                minsumpos=temp
            r-=1
        elif temp<0:
            if minsumneg<temp:
                minsumneg=temp
            l+=1
        else:
            minsumneg=0
            minsumpos=0
            break
    if abs(minsumpos)<abs(minsumneg):
        minsum=minsumpos
    else:
        minsum=minsumneg
    print(minsum)