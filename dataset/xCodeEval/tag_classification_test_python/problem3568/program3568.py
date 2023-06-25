def program3568():
    n, t = map(int,input().split())
    s = input()
    
    lista = []
    for l in s:
    	lista.append(l)
    
    for i in range(t):
    	c = False
    	for j in range(n-1):
    		if c:
    			c = False
    		elif lista[j] == "B" and lista[j+1] == "G":
    			lista[j] = "G"
    			lista[j+1] = "B"
    			c = True
    		
    
    saida = ""
    for l in lista:
    	saida += l
    	
    print(saida)