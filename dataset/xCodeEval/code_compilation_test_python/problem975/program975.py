def program975():
    n=input()
    x=input()
    
    if (n+5)/6%==0:
        l=1,0,2
    elif (n+4)/6%==0:
        l=1,2,0
    elif (n+3)/6%==0:
        l=2,1,0
    elif (n+2)/6%==0:
        l=2,0,1
    elif (n+1)/6%==0:
        l=0,2,1
    else:
        l=0,1,2
    
    print l[x]