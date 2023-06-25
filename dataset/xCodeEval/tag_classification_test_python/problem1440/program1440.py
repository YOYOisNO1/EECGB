def program1440():
    n, m = map(int, input().split());f = 0;
    while(n > 0):
    	s = input().split();
    	for ch in s:
    		if(ch != 'W' and ch != 'B' and ch != 'G'):	f = 1;
    	n -= 1;
    if(f == 0):	print("#Black&White");
    else:	print("#Color");