for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    while 1:
        j=l[0]
        l.remove(j)
        if j in l:
            l.remove(j)
        else:
            print(j)
            break