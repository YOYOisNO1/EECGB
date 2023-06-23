def program619():
    x = input()
    y =0
    for i in x:
    	if i=i.lower():
    		y+=1
    if y==1:
    	print x[0].upper()+x[1:].lower()
    else:
    	print x