for i in range(int(input())):
    s=input()
    l=[]
    prev=0
    res=""
    for x in range(len(s)):
        if s[x]==".":
            l.append(s[prev:x])
            prev=x+1
    l.append(s[prev:])
    for x in l[::-1]:
        res+=x+"."
    print(res[0:len(s)])
