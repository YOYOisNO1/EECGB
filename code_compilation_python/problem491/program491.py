def program491():
    s=input()
    j=len(s)
    try:
    	if s.index('1')<j-6 and s.count('0')>=6 and j>6:print('yes')
    	else:print('no')
    else:
    	print('no')