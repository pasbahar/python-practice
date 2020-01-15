for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    inc=l[0]
    exl=0
    for i in l[1:]:
        exl_n=max(exl,inc)
        inc=exl+i
        exl=exl_n
    print(max(inc,exl))