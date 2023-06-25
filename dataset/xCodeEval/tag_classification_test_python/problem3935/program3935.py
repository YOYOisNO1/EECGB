def program3935():
    x,y=map(int,input().split())
    x,y=y,x
    s=[]
    while x>0:
        d=x%y
        s.append(d)
        x//=y
    s.append(x)
    carry=0
    for n in range(len(s)):
        s[n]+=carry
        if s[n]==y:
            carry=1
            continue
        if 1<s[n]<y-1:
            print('NO')
            exit(0)
        carry=0
        if s[n]==y-1:
            carry=1
    print('YES')
    
    