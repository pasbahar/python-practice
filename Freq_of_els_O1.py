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
    i = 0
    while i<n: 
          
        # If this element is already processed, 
        # then nothing to do 
        if arr[i] <= 0: 
            i += 1
            continue
  
        # Find index corresponding to this element 
        # For example, index for 5 is 4 
        elementIndex = arr[i] - 1
  
        # If the elementIndex has an element that is not 
        # processed yet, then first store that element 
        # to arr[i] so that we don't loose anything. 
        if arr[elementIndex] > 0: 
            arr[i] = arr[elementIndex] 
  
            # After storing arr[elementIndex], change it 
            # to store initial count of 'arr[i]' 
            arr[elementIndex] = -1
              
        else: 
              
            # If this is NOT first occurrence of arr[i], 
            # then decrement its count. 
            arr[elementIndex] -= 1
  
            # And initialize arr[i] as 0 means the element 
            # 'i+1' is not seen so far 
            arr[i] = 0
            i += 1
    for x in range(n):
        arr[x]=-arr[x]
    print(*arr)
