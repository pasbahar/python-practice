for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    flag=0
    for i in range(n-1):
        if l[i]>l[i+1]:
            flag=1
            print(i+1)
    if not flag:
        print(0)