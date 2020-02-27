def mindist(s1,s2,n1,n2):
    t=[[0 for x in range(n1+1)] for x in range(n2+1)]
    for i in range(n1+1):
        t[0][i]=i
    for i in range(n2+1):
        t[i][0]=i
    for i in range(1,n2+1):
        for j in range(1,n1+1):
            if s1[j-1]==s2[i-1]:
                t[i][j]=t[i-1][j-1]
            else:
                t[i][j]=min(min(t[i-1][j],t[i][j-1]),t[i-1][j-1])+1
    return t[n2][n1]

for i in range(int(input())):
    n1,n2=map(int,input().split())
    s1,s2=input().split()
    print(mindist(s1,s2,n1,n2))
