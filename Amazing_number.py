def isprime(n):
    for i in range(2,int(n**0.5)+1,1):
        if n%i==0:
            return False
    return True

for i in range(int(input())):
    n=int(input())
    temp=n**0.5
    flag=0
    if int(temp)==temp:
        if isprime(temp):
            print(1)
            flag=1
    if not flag:
        print(0)
