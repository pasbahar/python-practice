for i in range(int(input())):
    n=int(input())
    arr=sorted(list(map(int,input().split())))
    minsumpos=9999999
    minsumneg=-9999999
    l,r=0,n-1
    while(l<r):
        temp=arr[l]+arr[r]
        if temp>0:
            if minsumpos>temp:
                minsumpos=temp
            r-=1
        elif temp<0:
            if minsumneg<temp:
                minsumneg=temp
            l+=1
        else:
            minsumneg=0
            minsumpos=0
            break
    if abs(minsumpos)<abs(minsumneg):
        minsum=minsumpos
    else:
        minsum=minsumneg
    print(minsum)