def program494():
    s = input()
    for i in range(len(s)):
    	if s[i] == '1':
    		s = s[i:]
    		break
    else:
    	s = ''
    if s.count('0') < 6:
    	print('no')
    else:
    	print('yes')