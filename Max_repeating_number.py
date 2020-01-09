for i in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=[0 for i in range(b)]
    for j in range(a):
        d[c[j]]+=1
    max1=0
    for i in range(b):
        if (d[i]>d[max1]):
            max1=i
    print(max1)