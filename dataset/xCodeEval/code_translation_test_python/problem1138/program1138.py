def program1138():
    n = int(input())
    p = n**(0.5)
    p1 = int(p)
    if p>p1:
        p1+=1
    if (p1**2)-(p1-1)<=n:
        print(p1*2)
    else:
        print( (p1*2)-1)