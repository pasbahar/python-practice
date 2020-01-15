for i in range(int(input())):
    n1,n2,k=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    i,j,ki=0,0,1
    flag=0
    while i<n1 and j<n2:
        if ki==k:
            print(min(l1[i],l2[j]))
            flag=1
            break
        if l1[i]<l2[j]: i+=1
        else:j+=1
        ki+=1
    while i<n1 and not flag:
        if ki==k:
            print(l1[i])
            flag=1
            break
        ki+=1
        i+=1
    while j<n2 and not flag:
        if ki==k:
            print(l2[j])
            break
        ki+=1
        j+=1        
