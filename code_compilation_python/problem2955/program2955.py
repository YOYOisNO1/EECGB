def program2955():
    #!/usr/bin/env python
    
    n=int(input())
    x=int(input())
    y=int(input())
    
    
    if x==1 and y==1: lost =4
    if x==n and y==n: lost = 4
    if x==1 and y>1 and y<n: lost =6
    if x==n and y>1 and y<n: lost =6
    if y==1 and x>1 and x<n: lost=6
    if y==n and x>1 and x<n: lost=6
    if y>1 and y< 2 and x>1 and x<2: lost =9
    
    if n*n>2*lost: print("YES")
    else: print("NO") 