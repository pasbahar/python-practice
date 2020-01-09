def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for i in range(int(input())):
    n=int(input())
    print(2,end=" ")
    for i in range(3,n,2):
        if isprime(i) and isprime(2*i+1):
            print(i,end=' ')
    print()