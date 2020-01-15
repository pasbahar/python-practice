def findpair(arr1,arr2,k):
    flag=0
    for i in arr1:
        if k-i in arr2:
            if not flag:
                flag=1
                print(i,end=" ")
                print(k-i,end="")
            else:
                print(',',i,end=' ')
                print(k-i,end="")
    if not flag: print(-1)
    else: print()



for i in range(int(input())):
    n1,n2,k=map(int,input().split())
    l1=sorted(list(map(int,input().split())))
    l2=list(map(int,input().split()))
    d2={}
    for i in l2:d2[i]=0
    findpair(l1,d2,k)