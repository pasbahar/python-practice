import math
for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    sum=0
    for i in l:
        sum+=math.ceil(i/k)
    print(sum)
