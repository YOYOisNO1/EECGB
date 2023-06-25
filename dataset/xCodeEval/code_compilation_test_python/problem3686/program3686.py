def program3686():
    n, bx= map(int, input().split())
    
    x= map(int, input().split())
    
    m, by= map(int, input().split())
    
    y=map(int, input().split())
    
    ret1= [x[a]*(bx**a) for a in range(0, len(x) )]
    r1=0
    for i=0 in range(0, len(ret1)):
    	r1+=ret1[i]
    
    ret2= [x[a]*(by**a) for a in range(0, len(y) )]
    r2=0
    for i=0 in range(0, len(ret1)):
    	r2+=ret2[i]
    
    if r1<r2 :
    	print '<'
    elif r2<r1:
    	print '>'
    else print '='