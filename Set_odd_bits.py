for i in range(int(input())):
    n=int(input())
    s=str(bin(n))[2:]
    l=list(s)
    for j in range(len(l)-1,0,-2):
        l[j]='1'
    s="".join(l)
    res=int(s,2)
    print(res)