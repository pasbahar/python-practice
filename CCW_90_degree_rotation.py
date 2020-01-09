for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n-1,-1,-1):
        k=0
        for j in range(n):
           print(l[i+k],end=" ") 
           k+=n
        
