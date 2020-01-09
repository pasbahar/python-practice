for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    low,high=0,n-1
    if n==1:
        print(l[0])
    elif l[0]>l[1]:
        print(l[0])
    elif l[n-1]>l[n-2]:
        print(l[n-1])
    else:
        while(low<=high):
            mid=(high+low)//2
            if l[mid]>l[mid-1] and l[mid]>l[mid+1]:
                print(l[mid])
                break
            elif l[mid]>l[mid-1]:
                low=mid+1
            else:
                high=mid-1
    