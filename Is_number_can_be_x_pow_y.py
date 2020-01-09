def ispower(n):
    flag=False
    for i in range(2,int(n**0.5)+1):
        p=n
        while(1):
            if p==1:
                flag=True
                break
            elif p%i==0:
                p/=i
            else:
                break
    if (flag or n==1):
        print(1)
    else:
        print(0)

for i in range(int(input())):
    n=int(input())
    ispower(n)
            