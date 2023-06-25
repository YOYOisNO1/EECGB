def program5154():
    import collections
    import math
    n,s,e = map(int,input().split())
    a =  bin(n)[2:]
    #print(a)
    n1 = len(a)
    #print(n1)
    #print(int('1'*n1,2))
    #print(s,e)
    result = 0
    #print('-----------')
    for i in xrange(n1):
    	b1= math.ceil(1.0*(s-2**i)/(2**(i+1))+1)
    	b2= math.floor(1.0*(e-2**i)/(2**(i+1))+1)
    	result +=(b2-b1+1)*int(a[i])
    	#print('-----')
    print(int(result))