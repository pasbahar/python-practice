for i in range(int(input())):
    s=list(input())
    flag=0
    for x in range(len(s)-1,0,-1):
        if s[x-1]<s[x]:
            ind=x-1
            flag=1
            break
    if flag==0:
        print("not possible")
    else:
        for j in range(len(s)-1,ind,-1):
            if s[j]>s[ind]:
                s[j],s[ind]=s[ind],s[j]
                break
        s1=s[0:ind+1]
        s2=sorted(s[ind+1:])
        s=s1+s2
        s=''.join(s)
        print(s)
