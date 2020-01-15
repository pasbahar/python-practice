for i in range(int(input())):
    s=input()
    count,lf,lf0=0,0,0
    for l in range(len(s)):
        if lf and lf0 and s[l]=='1':
            count+=1
            lf0=0
        if lf and s[l]=='0':
            lf0=1
        else:
            lf,lf0=0,0
        if s[l]=='1' and not lf:
            lf=1
    print(count)



