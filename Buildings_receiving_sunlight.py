for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=l[0]
    count=1
    for x in l:
        if x>m:
            count+=1
            m=x
    print(count)