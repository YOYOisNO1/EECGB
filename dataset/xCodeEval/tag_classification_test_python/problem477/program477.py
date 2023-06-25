def program477():
    import sys
    
    passwd = input()
    chars = {}
    for i in range(10):
    	chars[input()] = str(i)
    
    for i in xrange(0,80,10):
    	sys.stdout.write(chars[passwd[i:i+10]])
    print