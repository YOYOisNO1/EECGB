def program2401():
    n = int(input())
    str = input()
    str += '_'
    word_out = []
    word_in = []
    inpar = 0
    counter = 0
    for c in str:
    	if c == '(':
    		inpar = 1
    		if counter > 0:
    			word_out.append(counter)
    			counter = 0
    	elif c == ')':
    		inpar = 0
    		if counter > 0:
    			word_in.append(counter)
    			counter = 0
    	elif c == '_':
    		if inpar == 0 and counter > 0:
    			word_out.append(counter)
    		elif inpar == 1 and counter > 0:
    			word_in.append(counter)
    		counter = 0
    	else:
    		counter += 1
    
    if len(word_out) == 0:
    	print("0", end=' ')
    else:
    	print(int(max(word_out)), end=' ')
    print(int(len(word_in)))