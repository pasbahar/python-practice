for i in range(int(input())):
    n=int(input())
    res=[]
    
    for i in range(n+1):
        if i<10:
            res.append(str(i))
        else:
            s=str(i)
            flag=0
            for j in range(1,len(s)):
                if abs(int(s[j])-int(s[j-1]))!=1:
                    flag=1
                    break
            if not flag:
                res.append(s)
    print(*res)

        