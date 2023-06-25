def program2349():
    x = input()
    y = input()
    
    alf = 'abcdefghijklmnopqrstuvwxyz'
    
    z = ''
    
    for i in range(len(X)):
    	if y[i] == x[i]:
    		z += x[i]
    	elif alf.find(x[i]) < alf.find(y[i]):
    		z += y[i]
    	elif alf.find(x[i]) > alf.find(y[i]):
    		return -1
    return z