for i in range(int(input())):
    n=int(input())
    l=list(map(str,input().split()))
    d={"1":True,'2':True,'3':True}
    res=[]
    flag=0
    for s in l:
        for i in s:
            if i not in d:
                flag=1
                break
        if not flag:
            res.append(int(s))
        flag=0
    if len(res):
       print(*sorted(res))
    else:
        print(-1)
