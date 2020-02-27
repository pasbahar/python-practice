'''Given an array of N positive integers. Your task is to find the GCD of all numbers of the array.

Input:
First line of input contains number of test cases T. First line of test case contains a positive integer N, size of the array. Next line contains the array elements.

Output:
For each testcase, print the GCD of array elements.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= Arr[i] <= 106

Example:
Input:
1
2
5 10

Output:
5'''
for i in range(int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    minval=min(l)
    div=[]
    for j in range (1,minval+1):
        if minval%j==0:
            div.append(j)
    for k in l:
        for x in div[::-1]:
            if k%x==0:
                gcd=x
                break
            del div[-1]
    print(gcd)
