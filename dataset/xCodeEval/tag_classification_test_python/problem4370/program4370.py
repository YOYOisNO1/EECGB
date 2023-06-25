    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
def rotate_right(ind, c):
    	k = 0
    	i = ind
    	while True:
    		if LETTERS[i] == c:
    			return k, i
    		k = k + 1
    		i = (i + 1) % 26
    
def rotate_left(ind, c):
    	k = 0
    	i = ind
    	while True:
    		if LETTERS[i] == c:
    			return k, i
    		k = k + 1
    		i = i - 1
    		if i < 0:
    			i = 25
    
    s = input().upper()
    
    k = 0
    ind = 0
    for c in s:
    	k1, i1 = rotate_left(ind, c)
    	k2, i2 = rotate_right(ind, c)
    	if k1 < k2:
    		ind = i1
    		k = k + k1
    	else:
    		ind = i2
    		k = k + k2
    
    print(k)