def program1311():
    import sys
    
    sys.stdin.readline()
    str = sys.stdin.readline().split()[0]
    
    res = [len(x) for x in str.split("W+")]
    
    if res[-1] == 0:
    	res = res[:-1a]
    
    print len(res)
    
    for x in res:
    	print x,