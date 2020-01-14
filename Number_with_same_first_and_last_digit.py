for i in range(int(input())):
    n,k=map(int,input().split())
    c=0
    for x in range(n,k+1):
        s=str(x)
        if s[0]==s[-1]:
            c+=1
    print(c)

