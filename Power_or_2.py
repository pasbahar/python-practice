def ispower(n):
    if n==1:
        return "YES"
    if n==0:
        return "NO"
    while(n>=2):
        if(n%2!=0):
            return "NO"
        n/=2
    return "YES"

for i in range(int(input())):
    n=int(input())
    print(ispower(n))