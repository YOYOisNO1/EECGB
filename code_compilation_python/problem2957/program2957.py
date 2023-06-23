def program2957():
    #!/usr/bin/env python
    
    print "n=",
    n=int(input())
    print"x=",
    x=int(input())
    print "y=",
    y=int(input())
    
    
    if x==1 and y==1: lost =4
    if x==2*n and y==2*n: lost = 4
    if x==1 and y>1 and x<2*n: lost =6
    if y==1 and x>1 and x<2*n: lost=6
    if y>1 and y< 2*n and x>1 and x<2*n: lost =9
    
    if n*n>lost: print("YES")
    else: print " NO" 