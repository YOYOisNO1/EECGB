def program2437():
    n = input(); i = 1; j = 2, f = 0;
    if(n == 1):	print("YES");
    else:
    	while(i <= n):
    		if(i == n):	f = 1; print("YES");
    		i += (j += 1); if(f == 0):	print("NO");