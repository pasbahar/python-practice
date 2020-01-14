for i in range(int(input())):
    n=int(input())
    W=int(input())
    val=list(map(int,input().split()))
    wt=list(map(int,input().split()))

    c=[[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1]<=j:
                c[i][j]=max(c[i-1][j],val[i-1]+c[i-1][j-wt[i-1]])
            else:
                c[i][j]=c[i-1][j]
    print(c[n][W])