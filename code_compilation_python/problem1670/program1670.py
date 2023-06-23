def program1670():
    import sys
    
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    
    sum =0, count;
    for i in range(n):
    	s = sorted(a[:i])
    	temp = sum(s)
    	f =0
    	while temp + a[i] > m:
    		f+=1
    		temp -= s.pop()
    
    	print(f, end = " ")
    	
    