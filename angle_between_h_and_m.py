import math
for i in range(int(input())):
    h,m=map(float,input().split())
    if m==60:
        m=0
    if (abs(h*30-m*6+m/2)>180):
        print(math.floor(360-abs(h*30-m*6+m/2)))
    else:
        print(math.floor(abs(h*30-m*6+m/2)))