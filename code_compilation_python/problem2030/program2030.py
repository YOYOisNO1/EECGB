def program2030():
    import sys
    import itertools
    
    no = input()
    ans = input()
    l = len(no)
    ans = ans[-l::1]
    
    if int(ans[0])==0:
    	print "WRONG_ANSWER"
    	sys.exit()
    
    smallest = no
    
    permut in itertools.permutations(no, l):
    	#print permut
    	permut = "".join(list(permut))
    	if permut[0]!="0" and permut<smallest:
    		smallest = permut
    
    if ans==smallest:
    	print "OK"
    else:
    	print "WRONG_ANSWER"
    