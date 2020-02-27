'''Given a string, the task is to remove duplicates from it. Expected time complexity O(n) where n is length of input string and extra space O(1) under the assumption that there are total 256 possible characters in a string.

Note: that original order of characters must be kept same. 

Input:
First line of the input is the number of test cases T. And first line of test case contains a string.

Output: 
Modified string without duplicates and same order of characters.

Constraints: 
1 <= T <= 15
1 <= |string|<= 1000

Example:
Input:
2
geeksforgeeks
geeks for geeks

Output:
geksfor
geks for'''
for i in range(int(input())):
    l=input()
    s=''
    d={}
    for x in l:
        if x not in d.keys():
            d[x]=1
            s+=x
    print (s)