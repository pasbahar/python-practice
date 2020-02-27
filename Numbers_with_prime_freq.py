'''You are given an array of size N. You need to find elements which appear prime number of times in the array with minimum K frequency (frequency >= K).

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each testcase contains two lines of input:-
The size of the array N and minimum frequency K separated by a space.
The elements of the array separated by spaces.

Output:
For each testcase, print the elements that have prime frequency with their frequency >=K. Print the output in sorted order. If there are no such elements then print -1.

Constraints:
1<=T<=105
1<=N<=1000
1<=K<=10
1<=A[i]<=10000

Example:

Input:
2
13 2
11 11 11 23 11 37 51 37 37 51 51 51 51
3 1
11 22 33

Output:
37 51
-1'''
def isprime(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2,int(n**0.5)+1,1):
        if n%i==0:
            return False
    return True


for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    d={}
    res=[]
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d.keys():
        if isprime(d[i]) and d[i]>=k:
            res.append(i)
    res.sort()
    if len(res):
        print(*res)
    else:
        print(-1)
