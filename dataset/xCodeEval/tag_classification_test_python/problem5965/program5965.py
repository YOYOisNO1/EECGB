    from __future__ import division
    
def sgcd(a, b):
    	if a < b:
    		a, b = b, a
    	while b:
    		a, b = b, a % b
    	return a
    
def solve(C, Hr, Hb, Wr, Wb):
    	if Wb < Wr:
    		Wb, Wr = Wr, Wb
    		Hb, Hr = Hr, Hb
    
    	# if C // Wb < 30000:
    	# 	m = 0
    	# 	for b in xrange(C // Wb + 1):
    	# 		r = (C - b * Wb) // Wr
    	# 		h = r * Hr + b * Hb
    	# 		m = max(m, h)
    	# 	return m
    
    	gcd = sgcd(Wb, Wr)
    	lcm = (Wb * Wr) // gcd
    	assert lcm % Wb == 0 and lcm % Wr == 0
    	num_lcms = max(C // lcm - 1, 0)
    	Hb_lcm = (lcm // Wb) * Hb
    	Hr_lcm = (lcm // Wr) * Hr
    	if Hb_lcm > Hr_lcm:
    		# print('taking b')
    		x_lcm, y_lcm = num_lcms * (lcm // Wb), 0
    	else:
    		# print('taking r')
    		x_lcm, y_lcm = 0, num_lcms * (lcm // Wr)
    
    	m_lcms = x_lcm * Hb + y_lcm * Hr
    
    	C = C - num_lcms * lcm
    
    	m_rem = 0
    	x_rem, y_rem = 0, 0
    	for b in xrange(C // Wb + 1):
    		r = (C - b * Wb) // Wr
    		h = r * Hr + b * Hb
    		if h > m_rem:
    			m_rem = h
    			x_rem, y_rem = b, r
    		# m_rem = max(m_rem, h)
    
    	# print('lcm = %d, num_lcms = %d') % (lcm, num_lcms)
    	# print('Hb_lcm = %d, Hr_lcm = %d') % (Hb_lcm, Hr_lcm)
    	# print('x, y = %d, %d') % (x_lcm + x_rem, y_lcm + y_rem)
    	# print('x_lcm, x_rem = %d, %d') % (x_lcm, x_rem)
    	# print('y_lcm, y_rem = %d, %d') % (y_lcm, y_rem)
    
    	return m_lcms + m_rem
    
    if __name__ == '__main__':
    	C, Hr, Hb, Wr, Wb = [int(v) for v in input().split()]
    	m = solve(C, Hr, Hb, Wr, Wb)
    
    	print(m)