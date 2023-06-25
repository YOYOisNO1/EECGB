def program589():
     n = int(input())
    
    ent = map(int,input().split())
    
    media = sum(ent)/(n/2)
    
    
    indicesAcessados = []
    
    mapa = {}
    
    
    for i in range(n):
    	j = i+1
    	if i not in indicesAcessados:
    		soma = ent[i]
    		while j < n:	
    			if j in indicesAcessados:
    				j += 1
    			if soma + ent[j] == media:
    				mapa[i+1] = j+1
    				indicesAcessados.append(j)
    				break
    			j += 1
    		
    
    
    for i in mapa:
    	print i, mapa[i]