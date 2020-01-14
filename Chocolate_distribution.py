for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=int(input())
    l.sort()
    mini=1000000
    for x in range(n-m+1):
        diff=l[x+m-1]-l[x]
        if diff<mini:
            mini=diff
    print(mini)