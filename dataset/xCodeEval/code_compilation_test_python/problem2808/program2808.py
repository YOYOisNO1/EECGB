def program2808():
    s = 0
    t = 0
    for i in range(8):
        n = input()
        if n == 'BBBBBBBB':
        	s += 1
    	elif t == 0:
        	t = 1
        	s += n.count('B')
        else:
        	pass
    print(s)