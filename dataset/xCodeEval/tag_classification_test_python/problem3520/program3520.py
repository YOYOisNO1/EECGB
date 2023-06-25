def program3520():
    waste = input()
    s = input()
    m = -1
    for i in range(len(s)+1):
    	p = s[:i].count('0') + s[i:].count('1')
    	if p > m:
    		m = p
    print(m)