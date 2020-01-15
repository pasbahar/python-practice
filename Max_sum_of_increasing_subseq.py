def findmaxsum(arr):
    sums=[]
    for i in arr:
        sums.append(i)
    for i in range(len(arr)):
        j=0
        while(j<i):
            if arr[j]<arr[i] and sums[i]<sums[j]+arr[i]:
                sums[i]=sums[j]+arr[i]
            j+=1
    return max(sums)

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(findmaxsum(l))
