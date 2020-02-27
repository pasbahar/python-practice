'''Rishi is playing a game. Currently in the game, he is at a book fare in Pragati Maidan. There are total N kinds of books. In this game Rishi has to choose a book of particular kind and read it loudly as many times as he can in the given time and earn points.Rishi knows that reading a book of kind i needs Ai minutes and it will give him Bi points i.e,if he reads a particular book(i th type) m times he gets m*Bi points.

Rishi has been given K minutes for reading books. During this  time,he reads a book of a particular kind as many times as he can so as to maximize his points.
But he can not pick books of different kinds, he has to read the same book again and again.

Please help Rishi to find the maximal possible points.

Input:

First line contains single integer T denoting the number of test cases.
First line of each test case contains two integers N and K.
Next line contains N integers Ai denoting the time needed to read a book of kind i.
Next line contains N integers Bi denoting the points awarded after reading the ithth kind of book.
Output:
For each test case, print a single line containing maximal possible points.

Constraints:
1 <= T <= 100
1<=N<=105
1<=K<=109
1<=Ai,Bi<=109

Example:

Input
1
3 10
3 4 5
4 4 5
Output
12
Explanation:
Rishi has been 10 minutes to read the books ,So,

If Rishi picks book of first kind he can read it 3 times, he will get 3*4 = 12 points. 
If Rishi picks book of second kind he can read it 2 times, he will 2*4 = 8 points.
If Rishi picks book of third kind he can read it 2 times, he will get 2*5 = 10 points.

So the maximum possible points which he can earn in those 10 minutes is 12.'''
for i in range(int(input())):
    n,k=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    res=0
    for j in range(n):
        times=k//l1[j]
        points=times*l2[j]
        if res<points:
            res=points
    print(res)
