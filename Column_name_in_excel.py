def colname(n):
    temp=n
    res=[]
    rem,carry=0,0
    while(temp):
        rem=temp%26
        if not rem:
            rem=26
        temp=(temp-1)//26
        res.append(chr(int(ord('A')-1+rem)))
    return res

for i in range(int(input())):
    n=int(input())
    arr=colname(n)
    for i in arr[::-1]:
        print(i,end="")
    print()