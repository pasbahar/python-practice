
for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    j=0
    while (k>=l[j])and j<n-1:
        j+=1
    if j==n-1 and k>=l[j]:
        print(n-1)
    else:
        print(j-1)
        