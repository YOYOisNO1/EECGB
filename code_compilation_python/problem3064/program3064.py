def program3064():
    n=input()
    F=0
    for i in range(n):
        a,b=input()
        if abs(a-b)==1:
            F=1
    
        suma=suma+a
        sumb=sumb+b
    
    if suma%2==0 and sumb%2==0:
        print 0
    elif suma%2==1 and sumb%2==1:
        if F==1
            print 1
        else:
            print -1
    else:
        print -1