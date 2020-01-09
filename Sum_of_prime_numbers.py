def sumofprime(n):
    prime=[True for j in range(n+1)]
    for p in range(2,int(n**0.5)+1):
        if prime[p]==True:
            for j in range(p*2,n+1,p):
                prime[j]=False
    sum=0
    for j in range(2,n+1):
        if prime[j]:
            sum+=j
    return sum

for i in range(int(input())):
    n=int(input())
    print(sumofprime(n))

