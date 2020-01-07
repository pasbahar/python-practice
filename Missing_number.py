for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(n*(n+1)/2-sum(a))
    print(k)