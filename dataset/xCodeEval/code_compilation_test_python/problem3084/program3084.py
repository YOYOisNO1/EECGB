def program3084():
    l,r = [int(x) for x in input().split(" ")]
    
    if l==r:
    	return 0
    else:
    	print -1+(1<<(len('{0:b}'.format(l^r))))