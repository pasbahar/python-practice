for i in range(int(input())):
    s=input()
    d={}
    maxlen,currlen,prevind=1,0,0
    for j in range(len(s)) and d[s[j]]>=prevind:
        if s[j] in d.keys():
            currlen=j-d[s[j]]
            prevind=d[s[j]]
            d[s[j]]=j
        else:
            d[s[j]]=j
            currlen+=1
        if maxlen<currlen:
            maxlen=currlen
    print(maxlen)
