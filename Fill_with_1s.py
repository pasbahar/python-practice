import math
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    flag,count,max_count,s=0,0,0,0
    if not l[0]:
        try:
            count=l.index(1)
            max_count=count
        except:
            flag=1
            print(-1)
    if not flag:
        for i in range(1,n-1):
            if l[i]:
                count=i-1-s
                s=i
            if max_count<math.ceil(count/2):
                max_count=math.ceil(count/2)
    count=n-1-s
    if not l[-1]:
        count=n-1-s
        if max_count<count:
            max_count=count
    elif l[-1]:
        count=n-1-1-s
        if max_count<math.ceil(count/2):
            max_count=math.ceil(count/2)
    if not flag:
        print(max_count)

