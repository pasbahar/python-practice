'''Given a floor of dimensions 2 x W and tiles of dimensions 2 x 1, the task is to find the number of ways the floor can be tiled. A tile can either be placed horizontally i.e as a 1 x 2 tile or vertically i.e as 2 x 1 tile.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is W.

Output:
Print number of ways the floor can be tiled in a separate line.

Constraints:
1 ≤ T ≤ 50
1 ≤ W ≤ 70

Example:
Input
2
5
3

Output
8
3'''
def ways(n):
    l=[0]*(n+1)
    l[1]=1
    l[2]=2
    for i in range(3,n+1):
        l[i]=l[i-1]+l[i-2]
    return l[n]

for i in range(int(input())):
    n=int(input())
    print(ways(n))
