for i in range(int(input())):
    s1,s2=input().split()
    if sorted(s1)==sorted(s2):
        print('YES')
    else:
        print('NO')