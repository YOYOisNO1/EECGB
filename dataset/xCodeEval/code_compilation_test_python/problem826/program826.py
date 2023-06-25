    _ = input()
    s = input()
    i = 0
    out = ""
    while i < len(s):
    	if s[i] == "o" and if s[i+1] == "g" and if s[i+2] == "o":
    		i += 3 + howMany(i+3)
    	else:
    		out = out + s[i]
    		i += 1
    				
    
def howMany(n):
    	global s
    	gping = True
    	out = 0
    	while i < len(s) and going:
    		if s[n] == "g" and s[n+1] == "o":
    			out += 1
    		else:
    			going = False