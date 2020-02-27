def fib(n):
    fib1,fib2=1,1
    mod=pow(10,9)+7
    for i in range(n):
        fib3=(fib1+fib2)%mod
        fib1=fib2
        fib2=fib3
    return fib3


for i in range(int(input())):
    n=int(input())
    print(fib(n))