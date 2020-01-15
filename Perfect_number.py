def perfect(n):
    sm=0
    for i in range(1,n//2+1):
        if n%i==0:
            sm+=i
    if sm==n:
        return 1
    else: return 0

for i in range(int(input())):
    n=int(input())
    print(perfect(n))



