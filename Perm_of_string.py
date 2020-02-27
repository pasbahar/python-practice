'''Given a string S. The task is to print all permutations of a given string.

Input:
The first line of input contains an integer T, denoting the number of test cases. Each test case contains a single string S in capital letter.

Output:
For each test case, print all permutations of a given string S with single space and all permutations should be in lexicographically increasing order.

Constraints:
1 ≤ T ≤ 10
1 ≤ size of string ≤ 5

Example:
Input:
2
ABC
ABSG

Output:
ABC ACB BAC BCA CAB CBA 
ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA'''
def permut(arr,l,r):
    if l==r:
        res.append("".join(arr))
    for x in range(l,r):
        arr[x],arr[l]=arr[x],arr[l]
        permut(arr,l+1,r)
        arr[x],arr[l]=arr[l],arr[x]

for i in range(int(input())):
    arr=list(input().rstrip())
    res=list()
    permut(arr,0,len(arr))
    res.sort()
    for x in res:
        print(x,end=" ")
    print()
    res=[]