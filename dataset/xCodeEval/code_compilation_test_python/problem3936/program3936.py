def program3936():
    
    a,b,r=map(int,input().split())
    n=a*b/(4*r*r)
    
    if n==0:
        print "Second"
    else:
        print "First"