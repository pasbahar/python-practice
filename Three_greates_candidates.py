for i in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    print(max(l[0]*l[1]*l[-1],l[-1]*l[-2]*l[-3]))