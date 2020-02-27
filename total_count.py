'''Given an array of positive integers and a number K where K is used as threshold value to divide each element of the array into sum of different numbers. Find the sum of count of the numbers in which array elements are divided.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines. The first line of each test case consists of an integer N and K, where N is the size of array and K is the threshold value. The second line of each test case contains N space separated integers denoting array elements.

Output:
Corresponding to each test case, print the total count.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
0 ≤ Ai ≤ 107
1 ≤ K ≤ 107

Example:
Input:
1
4 3
5 8 10 13

Output:
14

Explanation:
Testcase 1: Each number can be expressed as sum of different numbers less than or equal to K as 5 (3 + 2), 8 (3 + 3 + 2), 10 (3 + 3 + 3 + 1), 13 (3 + 3 + 3 + 3 + 1). So, the sum of count of each element is 14.'''
import math
for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    sum=0
    for i in l:
        sum+=math.ceil(i/k)
    print(sum)
