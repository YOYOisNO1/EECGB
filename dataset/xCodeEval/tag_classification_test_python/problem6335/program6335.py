def program6335():
    s = input()
    m = dict()
    p1, p2 = 0, 0
    for idx, ch in enumerate(s):
    	if m.has_key(ch):
    		p1 = m[ch]
    		p2 = idx
    		break
    	else:
    		m[ch] = idx
    if abs(p1 - p2) == 1:
    	print('Impossible')
    	exit()
    # print(abs(p1) - p2 - 1)
    if abs(p1 - p2 - 1) % 2 == 0:
    	d = abs(p1 - p2 - 1) // 2
    	s1 = s[:p1 + 1]
    	s1 += s[p2 - 1: p2 - d: -1]
    	s2 = s[-1: p2: -1]
    	s2 += s[p1 + 1: p1 + d]
    else:
    	d = abs(p1 - p2 - 1) // 2
    	s1 = s[:p1 + 1]
    	s1 += s[p2 - 1: p2 - d: -1]
    	s2 = s[-1: p2: -1]
    	s2 += s[p1 + 1: p1 + d + 1]
    while len(s1) < len(s2):
    	s1 = s2[0] + s1
    	s2 = s2[1:]
    while len(s1) > len(s2):
    	s2 = s1[0] + s2
    	s1 = s1[1:]
    print(s1)
    print(s2)
    
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    # ABACDEFGHIJKLMNOPQRSTUVWXYZ
    # ABCDEFGHIJKLMNOPQRSGTUVWXYZ