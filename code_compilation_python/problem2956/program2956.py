def program2956():
    #!/usr/bin/env python
    
    print "n=",
    n=int(input())
    print"x=",
    x=int(input())
    print "y=",
    y=int(input())
    
    
    if x==1 and y==1: lost =4
    elif x==n and y==n: lost = 4
    elif x==1 and y>1 and x<n: lost =6
    elif y==1 and x>1 and x<n: lost=6
    else: lost =9
    
    if n*n>lost*2: print("YES")
    else: print " NO" 