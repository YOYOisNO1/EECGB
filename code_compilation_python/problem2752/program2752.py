def nextT(P):
    	P[1] += 1
    	if P[1]==60:
    		P[1] = 0
    		P[0] = (P[0] + 1)%24
    	return P
    
def palT(P):
    	h, m = P[0], P[1]
    	return h//10==m%10 and h%10==m//10
    
    T = [int(x) for x in input().split(':')]
    T = nextT(T)
    while not palT(T):
    	T = nextT(T)
    h, m = str(T[0]), str(T[1])
    if len(h)==1:
            h = '0' + h
    if len(m)==1:
            m = '0' + m
    print(h+':'+m
    #s = input()