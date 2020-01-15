def fib(n):
    fib1,fib2,fib3=1,1,2
    for i in range(2,n):
        fib4=fib1+fib2+fib3
        fib1=fib2
        fib2=fib3
        fib3=fib4
    if n<2:return fib1
    if n<3:return fib3
    else:return fib4

for i in range(int(input())):
    n=int(input())
    print(fib(n))