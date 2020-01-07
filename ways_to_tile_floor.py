def ways(n):
    l=[0]*(n+1)
    l[1]=1
    l[2]=2
    for i in range(3,n+1):
        l[i]=l[i-1]+l[i-2]
    return l[n]

for i in range(int(input())):
    n=int(input())
    print(ways(n))
