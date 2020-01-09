for i in range(int(input())):
    s=list(input())
    if s[0]==s[0].upper():
        for i in range(2,len(s),+2):
            s[i]=s[i].upper()
        for i in range(1,len(s),2):
            s[i]=s[i].lower()
    else:
        for i in range(2,len(s),+2):
            s[i]=s[i].lower()
        for i in range(1,len(s),2):
            s[i]=s[i].upper()
    for i in s:
        print(i,end="")
    print()