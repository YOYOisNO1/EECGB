def program1175():
    
    for i in range(n):
    	t = int(b[i])+t
    	k = int(b[n-i-1])+k
    
    	s=int(a[i])-c*t
    	s1=int(a[n-i-1])-c*k
    if s>s1:
    	print("Limak")
    if s1>s:
    	print("Radewoosh")