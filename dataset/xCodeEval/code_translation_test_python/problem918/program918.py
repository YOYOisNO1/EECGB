def ft(h, m):
    	sh = str(h)
    	if h < 10:
    		sh = '0' + sh
    	sm = str(m)
    	if m < 10:
    		sm = '0' + sm
    	return sh + ':' + sm
    	
def inc(hm):
    	h = hm[0]
    	m = hm[1]
    	m = (m + 1) % 60
    	if m == 0:
    		h = (h + 1) % 24
    	return (h, m)
    	
    H = input()
    s = 0
    while H != H[: : -1]:
    	hm = [int(H[: 2]), int(H[3: ])]
    	hm = inc(hm)
    	H = ft(hm[0], hm[1])
    	s += 1
    	
    print(s)