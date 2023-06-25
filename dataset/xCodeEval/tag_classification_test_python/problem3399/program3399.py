def program3399():
    a=list(input())
    b=list(input())
    c=list(input())
    d=list(input())
    q=list(input())
    w=list(input())
    e=list(input())
    r=list(input())
    z=0
    m=0
    for  i in range(1,8):
        if a[i-1]==a[i] and a[i]=='B':
            z+=1
        if z==7:
            m+=1
     
    z=0
    for  i in range(1,8):
        if b[i-1]==b[i] and b[i]=='B':
            z+=1
        if z>=7:
            m+=1
     
    z=0
    for  i in range(1,8):
        if c[i-1]==c[i] and c[i]=='B':
            z+=1
        if z>=7:
            m+=1
     
    z=0
    for  i in range(1,8):
        if d[i-1]==d[i] and d[i]=='B':
            z+=1
        if z>=7:
            m+=1
     
    z=0
    for  i in range(1,8):
        if q[i-1]==q[i]and q[i]=='B':
            z+=1
        if z==7:
            m+=1
     
    z=0
    for  i in range(1,8):
        if w[i-1]==w[i]and w[i]=='B':
            z+=1
        if z==7:
            m+=1
     
    z=0
    for  i in range(1,8):
        if e[i-1]==e[i] and e[i]=='B':
            z+=1
        if z==7:
            m+=1
     
    z=0
    for  i in range(1,8):
        if r[i-1]==r[i] and r[i]=='B':
            z+=1
        if z==7:
            m+=1
    if m!=8:
        for i in range(8):
            if a[i]==b[i] and b[i]==c[i] and c[i]==d[i] and d[i]==q[i] and q[i]==w[i] and w[i]==e[i] and e[i]==r[i] and a[i]=='B':
                m+=1
    print(m)