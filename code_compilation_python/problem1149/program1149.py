def program1149():
    k,a,b,v=map(int,input().split())
    box=0
    rem=a
    while rem>0:
        box+=1
        comp=0
        if (b>k-1):
            comp=k
            b-=k-1
        else:
            comp=b+1
            b=0
        rem-=v*comp
    print box
            