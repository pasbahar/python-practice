'''Given an array A[] of N positive integers which can contain integers from 1 to N where elements can be repeated or can be absent from the array. Your task is to count frequency of all elements from 1 to N.

Note: Expected time complexity is O(n) with O(1) extra space.

Input:
First line of input contains an integer T denoting the number of test cases. For each test case, first line contains an integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
For each test case, output N space-separated integers denoting the frequency of each element from 1 to N.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106
1 <= A[i] <= 106

Example:
Input:
2
5
2 3 2 3 5
4
3 3 3 3

Output:
0 2 2 0 1
0 0 4 0

Explanation:
Testcase 1: Counting frequencies of each array elements, we have:
1 occurring 0 times.
2 occurring 2 times.
3 occurring 2 times.
4 occurring 0 times.
5 occurring 1 time.'''
for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
     # Subtract 1 from every element so that  
    # the elements become in range from 0 to n-1  
    for j in range(n): 
        arr[j] = arr[j] - 1
  
    # Use every element arr[i] as index  
    # and add 'n' to element present at  
    # arr[i]%n to keep track of count of  
    # occurrences of arr[i]  
    for i in range(n): 
        arr[arr[i] % n] = arr[arr[i] % n] + n 
  
    # To print counts, simply print the  
    # number of times n was added at index  
    # corresponding to every element  
    for i in range(n): 
        print(arr[i] // n,end=" ")
    print() 