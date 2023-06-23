def program614():
    k,n,s,p=map(int,input().split())
    m=int()
    kl=int()
    if n % s ==0:
    	kl = n // s
    	else:
    		kl = n // s + 1
    vl = kl * k
    if vl % p == 0:
    	m = vl // p
    else: m = vl // p + 1
    print (m)