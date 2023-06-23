def program1609():
    s = list(input())
    t = list(input())
    
    i = len(s) - 1;
    
    while (s[i] == 'z') :
    	i -= 1
    
    s[i] = chr(ord(s[i]) + 1)
    
    if s < t :
    	print s
    else
    	print "No such string"