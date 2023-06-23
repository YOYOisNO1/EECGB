def program2467():
    n,m=map(int,input().split())
    s=[0,0]
    for i in range(2):
        pet = 0
        vas = 0
        r=n;b=m
        if i==0:
            c='r'
            r-=1
        else:
            c='b'
            b-=1
        l=False
        while r and b:
            if not l:
                if c[-1]=='r':
                    c+='b'
                    b-=1
                else:
                    c+='r'
                    r-=1
                vas+=1
                l=not l
            else:
                if c[-1]=='r':
                    c+='r'
                    r-=1
                else:
                    if c[-1] == 'b':
                        c += 'b'
                        b -= 1
                pet+=1
                l=not l
        if b:
            if c[-1]=='b':
                pet+=1
            else:
                vas+=1
            c+='b'*b
            pet+=(b-1)
        else:
            if c[-1]=='r':
                pet+=1
            else:
                vas+=1
            c+='r'*r
            pet+=r-1
        if pet>=s[0]:
            s[0]=pet
            s[1]=vas
    print(*s)