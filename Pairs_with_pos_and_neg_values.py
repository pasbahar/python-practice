'''Given an array of distinct integers, print all the pairs having positive value and negative value of a number that exists in the array.

NOTE: If there is no such pair in the array , print "0".

Input:
The first line consists of an integer T i.e number of test cases. The first line of each test case consists of an integer n.The next line of each test case consists of n spaced integers.

Output:
Print all the required pairs in the increasing order of their absolute numbers.

Constraints: 
1<=T<=100
1<=n<=1000
-1000<=a[i]<=1000

Example:
Input:
2
6
1 -3 2 3 6 -1
8
4 8 9 -4 1 -1 -8 -9

Output:
-1 1 -3 3 
-1 1 -4 4 -8 8 -9 9 '''
for i in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    res=[]
    left=0
    right=n-1
    while(left<right):
        if -l[left]>l[right]:
            left+=1
        elif -l[left]<l[right]:
            right-=1
        else:
            res.append(l[right])
            res.append(l[left])
            left+=1
            right-=1
    res=res[::-1]
    if len(res)==0:
        print(0)
    else:
        print(*res)
        
