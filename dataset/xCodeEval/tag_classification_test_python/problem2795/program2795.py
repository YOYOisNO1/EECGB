def program2795():
    w,h=[int(s) for s in input().split()]
    u1,d1=[int(s) for s in input().split()]
    u2,d2=[int(s) for s in input().split()]
    if d1>h or d1==0:
        u1=0
        d1=0
    if d2>h or d2==0:
        u2=0
        d2=0
    #print(h*(h+1)//2)
    if d1<d2:
        d1,d2=d2,d1
        u1,u2=u2,u1
    w=max(0,w+(d1+h)*(h-d1+1)//2-u1)
    #print(w)
    w=max(0,w+(d2+d1-1)*(d1-d2)//2-u2)
    #print(w)
    w+=(d2-1)*(d2)//2
    print(w)
    