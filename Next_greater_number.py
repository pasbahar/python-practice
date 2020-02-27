'''Given a number n, find the smallest number that has same set of digits as n and is greater than n. If x is the greatest possible number with its set of digits, then print “not possible”.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is n,n is the number.

Output:

Print the greater number than n with same set of digits and if not possible then print "not possible" without double quote.

Constraints:

1 ≤ T ≤ 100
1 ≤ n ≤ 100000

Example:

Input
2
143
431

Output
314
not possible'''
for i in range(int(input())):
    s=list(input())
    flag=0
    for x in range(len(s)-1,0,-1):
        if s[x-1]<s[x]:
            ind=x-1
            flag=1
            break
    if flag==0:
        print("not possible")
    else:
        for j in range(len(s)-1,ind,-1):
            if s[j]>s[ind]:
                s[j],s[ind]=s[ind],s[j]
                break
        s1=s[0:ind+1]
        s2=sorted(s[ind+1:])
        s=s1+s2
        s=''.join(s)
        print(s)
