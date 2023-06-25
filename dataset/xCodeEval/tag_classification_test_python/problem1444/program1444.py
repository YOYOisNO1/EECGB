def program1444():
    m,n=map(int,input().split())
    l=[]
    for i in range(m) :
        x=list(map(str,input().split()))
        for j in x :
            l.append(j)
    if 'C' in l or 'Y' in l or 'M' in l:
        print("#Color")
    else :
        print("#Black&White")
        