def program324():
    N = int(input())
    s = ""
    
    for i in range(1,N+1):
    	s += str(i)
    
    print(s[N-1])