    x, y = input().split(" ")
    
    x = int(x)
    y = int(y)
    
    
    
    
    
def ebob(a,b):
    	while b:
    		a,b=b,a%b;
    	return a;
    
def ebobb(*args):
    	return reduce(ebob, args)
    
def ekok(a,b):
    	return a*b/ebob(a,b);
    
def ekokk(*args):
        return reduce(ekok, args)
    
    
    
    if (x<=20) and (y<=20):
        carpim=1
        carpims=1
        for i in range(x):
            carpim*=i+1
    
        for i in range(y):
            carpims*=i+1
        k =ebob(carpim, carpims)
        print(k)
    
    elif (x>=20) and (y<=20) :
        carpim=1
        carpims=1
        for i in range(y):
            carpims*=i+1
        print(carpims)
    
    elif (x<=20) and (y>=20) : 
        carpim=1
        carpims=1
        for i in range(x):
            carpim*=i+1
        print(carpim)
    
    elif (x>=20) and (y>=20) and (x<y) :
        carpim=1
        carpims=1
        for i in range(x):
            carpim*=i+1
        print(carpim)
        
    elif (x>=20) and (y>=20) and (x>y) :
        carpim=1
        carpims=1
        for i in range(y):
            carpims*=i+1
        print(carpims)
    