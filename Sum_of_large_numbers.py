for i in range(int(input())):
    n1,n2=map(int,input().split())
    res=str(n1+n2)
    if len(res)==len(str(n1)):
        print(res)
    else:
        print(n1)
