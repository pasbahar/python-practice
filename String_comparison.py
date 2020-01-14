def compare(s1,s2):
    if s1==s2:
        return 0
    elif s1.find('ng')!=-1 or s2.find!=-1:
        s1=s1.replace('ng','N')
        s2=s2.replace('ng','N')
        x=0
        while x<len(s1)and x<len(s2):
            if s1[x]!=s2[x]:
                if s1[x]=='N':
                    if s2[x]<='n':
                        return 1
                    else:
                        return -1
                if s2[x]=='N':
                    if s1[x]<='n':
                        return -1
                    else:
                        return 1
            if s1[x]>s2[x]:
                return 1
            if s1[x]<s2[x]:
                return -1
            x+=1
        if len(s1)>len(s2):
            return 1
        else:
            return -1
    else:
        if s1<s2:
            return -1
        elif s1>s2:
            return 1

       
for i in range(int(input())):
    s1,s2=map(str,input().split())
    print(compare(s1,s2))