for i in range(int(input())):
    a1,a2=map(int,input().split())
print(list(bin(a1^a2)).count('1'))
