       
     
def solve(n_homer=0, n_medea=0):
        global number, n
        
        if (n_homer, n_medea) in mem:
    		return mem[n_homer, n_medea][0]
        
        best = [0, 0]
        pos = n_homer + n_medea
        
        if n_homer < n:
            aux = solve(n_homer + 1, n_medea)[:]
            aux[0] = int(number[pos] + str(aux[0]))
            if sum(best) < sum(aux):
    			mem[n_homer, n_medea] = aux[:], 'H'
    			best = aux[:]
            
        if n_medea < n:
            aux = solve(n_homer, n_medea + 1)[:]
            aux[1] = int(number[pos] + str(aux[1]))
            if sum(best) < sum(aux):
    			mem[n_homer, n_medea] = aux[:], 'M'
    			best = aux[:]
            
        return best[:]
       
       
    mem = {}
    n = input()
    number = input()
    
    # print solve()
    
    solution = ""
    n_homer, n_medea = 0, 0
    
    while n_homer < n or n_medea < n:
    	if mem[n_homer, n_medea][1] == 'H':
    		n_homer += 1
    		solution += 'H'
    	else:
    		n_medea += 1
    		solution += 'M'
    		
    print solution