for i in range (int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=int(input())
    in1,in2=-1,-1
    for x in l:
        if x==k and in1==-1:
            in1=l.index(x)
        if in1!=-1 and x!=k:
            in2=l.index(x)-1
            break
    if in1!=-1 and in2==-1:
        in2=len(l)-1
    if in1==-1:
        print(-1)
    else:
        print(in1,in2)
