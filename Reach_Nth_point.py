for i in range(int(input())):
    n=int(input())
    res=0
    a,b,=1,1
    for x in range(n-1):
        res=a+b
        a=b
        b=res
    print(res)