def val(pair):
    	s = 0
    	if pair[0] != '':
    		s += int(pair[0])
    	if pair[1] != '':
    		s += int(pair[1])
    	return s
     
def solve(n_homer=0, n_medea=0):
        global number, n
        
        if (n_homer, n_medea) in mem:
    		return mem[n_homer, n_medea][0]
        
        best = ['', '']
        pos = n_homer + n_medea
        
        if n_homer < n:
            best = solve(n_homer + 1, n_medea)[:]
            best[0] = number[pos] + str(best[0])
            mem[n_homer, n_medea] = best, 'H'
            
        if n_medea < n:
            aux = solve(n_homer, n_medea + 1)[:]
            aux[1] = number[pos] + str(aux[1])
            if val(best) < val(aux):
    			best = aux
    			mem[n_homer, n_medea] = best, 'M'
    			
    	
        return best
       
       
    mem = {}
    n = input()
    number = input()
    
    solve()
    
    # for k in sorted(mem.keys()):
    #     print k, mem[k]
    
    
    solution = ""
    n_homer, n_medea = 0, 0
    
    while n_homer < n or n_medea < n:
    	# print solution
    	if mem[n_homer, n_medea][1] == 'H':
    		n_homer += 1
    		solution += 'H'
    	else:
    		n_medea += 1
    		solution += 'M'
    		
    print solution