def program4534():
    p,d,t,f,c=[int(input())for _ in'12345']
    r=0
    while p<d:
    	z=(p*t)/(d-p)
    	if z*d>=c:break
    	t+=2*z+f;r+=1
    print(r)