'''Given an array A of N integers, find a combination of four elements in the array whose sum is equal to a given value X.

Input:
First line consists of T test cases. First line of every test case consists of an integer N, denoting the number of elements in an array. Second line consists of N spaced array elements. Third line of every test case X.

Output:
Single line output, print 1 if combination is found else 0.

Constraints:
1 <= T <= 100
1 <= N <= 106

Example:
Input:
1
6
1 5 1 0 6 0
7
Output:
1

Explantion:
Testcase 1: 1, 5, 1, 0 are the four elements which makes sum 7.'''
def sumof4(arr,k,n):
    for i in range(n):
        for j in range(i+1,n):
            for l in range(j+1,n):
                for g in range(l+1,n):
                    sum=arr[i]+arr[j]+arr[l]+arr[g]
                    if sum==k:
                        return 1
                    elif sum>k:
                        break
                if arr[i]+arr[j]+arr[l]>k:break
            if arr[i]+arr[j]>k:break    
        if arr[i]>k:break
    return 0


for i in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    k=int(input())
    print(sumof4(l,k,n))