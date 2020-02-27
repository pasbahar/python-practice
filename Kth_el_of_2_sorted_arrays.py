'''Given two sorted arrays A and B of size M and N respectively and an element k. The task is to find the element that would be at the k’th position of the final sorted array.

Input:
First line consists of test cases T. First line of every test case consists of 3 integers N, M and K, denoting M number of elements in A, N number of elements in B and kth position element. Second and Third line of every test case consists of elements of A and B respectively.

Output:
Print the element at the Kth position.

Constraints:
1 <= T <= 200
1 <= N, M <= 106
1 <= Ai, Bi <= 106
1 <= K <= N+M

Example:
Input:
1
5 4 5
2 3 6 7 9
1 4 8 10

Output:
6

Explanation:
Testcase 1: Element at 5th position after merging both arrays will be 6.'''
for i in range(int(input())):
    n1,n2,k=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    i,j,ki=0,0,1
    flag=0
    while i<n1 and j<n2:
        if ki==k:
            print(min(l1[i],l2[j]))
            flag=1
            break
        if l1[i]<l2[j]: i+=1
        else:j+=1
        ki+=1
    while i<n1 and not flag:
        if ki==k:
            print(l1[i])
            flag=1
            break
        ki+=1
        i+=1
    while j<n2 and not flag:
        if ki==k:
            print(l2[j])
            break
        ki+=1
        j+=1        
