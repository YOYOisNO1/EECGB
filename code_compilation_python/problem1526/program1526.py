def program1526():
    a,b,c,d=map(int,input().split())
    if a==c or b==d:
        q=1
    else:
        q=2
    if (a+b)%2==(c+d)%2:
    
        if abs(c-a)==abs(b-d):
            w=1
        else:
            w=2
    else:
        w=0
    else:
        w=0
    e=max(abs(a-c),abs(b-d))
    print(q,w,e)