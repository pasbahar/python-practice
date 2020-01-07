def ismajor(arr,n):
    dict={}
    for x in arr:
        if x in dict.keys():
            dict[x]+=1
            if dict[x]>n/2:
                return x
        else:
            dict[x]=1
    return -1

for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(ismajor(arr,n))