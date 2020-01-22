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