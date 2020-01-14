for i in range(int(input())):
    s=input()
    ch=input()
    c=int(input())
    count,ind=0,-1
    for j in range(len(s)):
        if s[j]==ch:
            count+=1
        if count==c:
            ind=j+1
            break
    if c==0:
        print(s)
    elif ind!=-1 and ind!=len(s):
        s=list(s)
        s=s[ind:]
        s=''.join(s)
        print(s)
    else:
        print('Empty string')