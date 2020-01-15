for i in range(int(input())):
    n=int(input())
    l=list(map(str,input().split()))
    d={}
    for i in l:
        if i in d:
            d[i]+=1
        else: d[i]=1
    mx=max(d.values())
    winner=str(max(d.keys()))
    for i in d.keys():
        if d[i]==mx and winner>str(i):
            winner=str(i)
    print(winner, mx, end=" ")
    print()
