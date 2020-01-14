
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    prod=1
    for x in l:
        prod*=x
    for x in l:
        print(prod//x,end=" ")
    print()