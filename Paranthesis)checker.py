'''Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

Input:
The first line of input contains an integer T denoting the number of test cases.  Each test case consists of a string of expression, in a separate line.

Output:
Print 'balanced' without quotes if the pair of parenthesis is balanced else print 'not balanced' in a separate line.

Constraints:
1 ≤ T ≤ 100
1 ≤ |s| ≤ 105

Example:
Input:
3
{([])}
()
([]

Output:
balanced
balanced
not balanced'''
def isopening(c):
    if c=='{'or c=='['or c=='(':
        return True
    else: return False

def isbalanced(s):
    d={'{':'}','[':']','(':')'}
    braces=[]
    for i in s:
        if isopening(i): 
            braces.append(i)
        elif len(braces):
            c=braces[-1]
            if i!=d[c]:
                return 'not balanced'
            braces.pop(-1)
        else:
            return 'not balanced'
    if len(braces): return 'not balanced'
    else: return 'balanced'


for i in range(int(input())):
    s=input()
    print(isbalanced(s))