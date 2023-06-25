def fn(s):
        if len(s) == 1:
            if s[0] == '0':
                print "No"
            else:
                print "Yes"
    	else:
    		c = s[0]
    		for i in s:
    			if i != c:
    				print "No"
    				return
    			c = str((int(c) + 1) % 2)
    	print "Yes"
    	
    if __name__ == '__main__':
    	n = input()
    	s = input()
    	fn(s)