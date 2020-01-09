for i in range(int(input())):
    s=bin(int(input()))
    l=list(s)
    l=l[2:]
    if l==l[::-1]:
        print(1)
    else:
        print(0)


