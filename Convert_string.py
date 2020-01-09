for i in range(int(input())):
    s=input()
    ans=str()
    v=['A', 'E', 'I','O','U','a','e','i','o','u']
    for i in s:
        if i not in v:
            if i.islower():
                ans+='#'+i.upper()
            else:
                ans+='#'+i.lower()
    if len(ans)==0:
        print(-1)
    else:
        print(ans)