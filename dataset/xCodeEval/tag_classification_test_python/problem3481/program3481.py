    import math
def main():
    	s=input();
    	p=s.split(' ')
    	t=long(p[0])
    	b=long(p[1])
    	w=long(p[2])
    	g=gcd(b,w)
    	l=b*w/g
    	ans=t/l*min(w,b)
    	ans+=min(w-1,b-1,t-t/l*l)
    	div=gcd(ans,t)
    	pr= str(ans/div)+"/"+str(t/div)
    	print(pr)
def gcd(a, b):
        """Calculate the Greatest Common Divisor of a and b.
    
        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
        while b:
            a, b = b, a%b
        return a
    main()
    