for i in range(int(input())):
    n=int(input())
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)