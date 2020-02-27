'''You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of four lines.
The first line consists of N the number of items.
The second line consists of W, the maximum capacity of the knapsack.
In the next line are N space separated positive integers denoting the values of the N items,
and in the fourth line are N space separated positive integers denoting the weights of the corresponding items.

Output:
For each testcase, in a new line, print the maximum possible value you can get with the given conditions that you can obtain for each test case in a new line.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 1000
1 ≤ W ≤ 1000
1 ≤ wt[i] ≤ 1000
1 ≤ v[i] ≤ 1000

Example:
Input:
2
3
4
1 2 3
4 5 1
2
3
1 2 3
4 5 6
Output:
3
1'''
for i in range(int(input())):
    n=int(input())
    W=int(input())
    val=list(map(int,input().split()))
    wt=list(map(int,input().split()))

    c=[[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1]<=j:
                c[i][j]=max(c[i-1][j],val[i-1]+c[i-1][j-wt[i-1]])
            else:
                c[i][j]=c[i-1][j]
    print(c[n][W])