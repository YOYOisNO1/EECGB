def program1269():
    a,b = map(int,input.split())
    i=0
    while(a-b<=0):
    	a=3*a
    	b=2*b
    	i++	
    print(i)	