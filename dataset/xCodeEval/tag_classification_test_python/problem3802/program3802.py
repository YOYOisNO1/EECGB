def program3802():
    x = [int(e) for e in input().split(" ")]
    x1 = [int(t) for t in input().split(" ")]
    y = [int(w) for w in input().split(" ")]
    y1 = [int(q) for q in input().split(" ")]
    
    indx1 = len(x1)-1 #último item da lista
    indy1 = len(y1)-1 #último item da lista
    basex = x[1]
    basey = y[1]
    lx = x[0]
    ly = y[0]
    somx = 0
    somy = 0
    
    k = 0
    h = 0
    while (lx > 0):
    	somx += (x1[indx1]*(x[1]**k))
    	indx1 -= 1
    	k += 1
    	lx -= 1
    while (ly > 0):
    	somy += (y1[indy1]*(y[1]**h))
    	indy1 -= 1
    	h += 1
    	ly -= 1
    
    if(somx == somy):
    	print("=")
    elif (somx > somy):
    	print(">")
    elif (somx < somy):
    	print("<")
    else:
    	pass