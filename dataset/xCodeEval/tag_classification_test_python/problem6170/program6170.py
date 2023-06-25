def program6170():
    r=lambda:map(int,input().split())
    a,b,c,d=r()
    print(1) if a==c or b==d else 2,
    print(0) if (a+b)&1 != (c+d)&1 else (1 if a+b==c+d or a-c==b-d else 2),
    print(max(abs(a-c),) abs(b-d))