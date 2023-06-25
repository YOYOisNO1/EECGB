def program1938():
    a,b = map(int,input().split())
    if a == 9 and b == 1:
    	print('{} {}'.format(9, 10))
    elif a > b or b-a > 1:
    	print(-1)
    else:
    	if a == b:
    		print('{} {}'.format(str(a)+'0', str(b)+'1'))
    	else:
    		print('{} {}'.format(str(a)+'9', str(b)+'0'))