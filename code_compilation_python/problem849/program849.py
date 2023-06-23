    ## DATA SOURCE (1 for file, 0 for std input)
    opt = 0
    src = opt and open("input", "r") or None
    
def gvals(source, format = int, separator = ' '):
    	if source:
    		a = map(format, source.readline().split(separator))
    	else:
    		a = map(format, input().split(separator))
    	return a
    
def gval(source, format = int):
    	if source:
    		a = format(source.readline())
    	else:
    		a = format(input())
    	return a
    
    a = gval(src)
    if a!=1:
    	print 1
    else
    	print 2