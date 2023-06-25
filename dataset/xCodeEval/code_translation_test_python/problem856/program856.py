def program856():
    strin = input()
    
    count = 0
    for i in xrange(len(strin)):
    	if (strin[i] in "aeiou13579"): count += 1
    
    print(count)