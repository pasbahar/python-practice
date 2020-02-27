'''Given a string of lowercase alphabets and a number k, the task is to print the minimum value of the string after removal of ‘k’ characters.  The value of a string is defined as sum of squares of count of each distinct character. For example consider the string “saideep”, here frequencies of characters are s-1, a-1, i-1,e-2, d-1, p-1 and value of the string is 1^2 + 1^2 + 1^2 + 1^2 + 1^1 + 2^2 = 9.

Input:
The first line of input contains the number T denoting the no of test cases . Then T test cases follow. Each test case contains two lines.The first line of each test case contains a string str. The second line of each test case consist of an integer k .

Output:
The output for each test case will be an integer denoting the min possible value of the string.

Constraints:
1<=T<=100 
1<=str<=50
1<=k<=50

Example:
Input
2
abccc
1
aaab
2
Output
6
2'''
for i in range(int(input())):
    s=input()
    k=int(input())
    d={}
    res,flag=0,0
    for x in s:
        if x in d.keys():
            d[x]+=1
        else:
            d[x]=1
    l=sorted(list(d.values()))
    sz=len(l)
    if sum(l)<=k:
        print(0)
        flag=1
    while(k>0 and not flag):
        j=sz-1
        while k>0:
            l[j]-=1
            j-=1
            k-=1
            if(l[j+1]+1!=l[j]):
                break
    if not flag:
        for x in l:
            res=res+x*x
        print(res)
