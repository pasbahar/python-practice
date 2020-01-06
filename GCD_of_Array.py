for i in range(int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    minval=min(l)
    div=[]
    for j in range (1,minval+1):
        if minval%j==0:
            div.append(j)
    for k in l:
        for x in div[::-1]:
            if k%x==0:
                gcd=x
                break
            del div[-1]
    print(gcd)
