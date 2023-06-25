def program1852():
    n=int (input ())
    ch= input()
    l=ch.split()
    m=0
    for i in l :
        s=0
        for j in i :
            if j==j.upper():
                s=s+1
            m=max(m,s)
    
    print(m)
                