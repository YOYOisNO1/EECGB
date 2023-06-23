    
def checar_letras(s,t):
    	i = 0
    	for e in s[i::]:
    		if e in t[i::]:
    			continue
    		else:
    			return False	
    		i+=1
    	return True
    
def tirar_letras(s,t):
    	i = 0
    	while i < len(s) -1:
    		if not s[i] in t:
    			if i+1 < len(s):
    				s = s[:i:] + s[i+1::]
    			else:
    				s = s[:i:]
    		i +=1	
    
def  resposta(s,t):
    	
    	if len(t) == len(s) and checar_letras(t,s):   #OK
    		return  "array"
    	
    	if checar_letras(t,s) == False:           #OK
    		return  "need tree"
    	
    	if t in s or checar_letras(t,s):
    		return "automaton"
    	if:
    		return "both"
    
    s = input()
    t = input()
    
    print resposta(s,t)
    
    
    	