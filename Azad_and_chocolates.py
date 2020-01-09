def istrue(n):
    for i in range(n//3+1):
        y=n-3*i
        if y%7==0:
            return 1
    return 0

for i in range(int(input())):
    n=int(input())
    print(istrue(100-n))