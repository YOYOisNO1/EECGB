    from queue import Queue
    
def bfs(x, y):
    	if x == y:
    		return 0
    	dicionario = {}
    	visitas = [False] * 10010
    	fila = Queue()
    	fila.put(x)
    	visitas[x] = True
    	dicionario[x] = 0
    
    	while True:
    		t = fila.get()
    		if t == y:
    			return dicionario[t]
    		ba = t - 1
    		bv = t * 2
    
    		if 0 < bv < 10010 and not visitas[bv]:
    			dicionario[bv] = dicionario[t] + 1
    			visitas[bv] = True
    			fila.put(bv)
    		if 0 < ba <10010 and not visitas[ba]:
    			dicionario[ba] = dicionario[t] + 1
    			visitas[ba] = True
    			fila.put(ba)
    
    x,y = map(int, input().split())
    print(bfs(x,y))
    #