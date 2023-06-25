def program4323():
    a=int(input())
    b=int(input())
    c=int(input())
    xa=a
    xb=b/2
    xc=c/4
    
    if xa<xb:
    	if xa<xc:
    		x = 7*xa
    	else:
    		x = 7*xc
    else:
    	if xb < xc:
    		x=7*xb
    	else:
    		x=7*xc
    print(x)