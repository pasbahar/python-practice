for i in range(int(input())):
    n=int(input())
    if(n%3==0):
        print(n//3-1,n//3,n//3+1)
    else:
        print(-1)