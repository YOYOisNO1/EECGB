    # strs = [input() for _ in range(3)]
    
def main():
    	n = int(input())
    	s = input()
    
    	r = g = b = 0
    	for c in s:
    		if c == 'R':
    			r += 1
    		elif c == 'G':
    			g += 1
    		else:
    			b += 1
    	ss = r + g + b
    	l = [(r, 'R'), (g, 'G'), (b, 'B')]
    	l.sort()
    	l1, l2, l3 = l
    	c1, s1 = l1
    	c2, s2 = l2
    	c3, s3 = l3
    
    	if c2 == 0:
    		s = [s3]
    	elif c1 == 0:
    		if c2 == 1:
    			if c3 == 1:
    				s = [s1]
    			else:
    				s = [s1, s2]
    		else:
    			s = [s1, s2, s3]
    	else:
    		s = [s1, s2, s3]
    
    	s.sort()
    	print(''.join(s))
    
    
    
    main()
    
    