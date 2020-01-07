def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        f=[]
        f.append(0)
        f.append(1)
        for i in range(2,n+1):
            f.append(f[i-1]+f[i-2])
        return f[n]%1000000007

for i in range(int(input())):
    print(fib(int(input())))