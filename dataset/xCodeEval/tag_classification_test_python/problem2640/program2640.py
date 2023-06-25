def program2640():
    R=lambda:map(int,input().split())
    v=[];f=[];p=s=0
    n,m=R()
    for i in R():
    	s+=i
    	g=s
    	while s>m:
    		s-=f[-1-p]
    		p+=1
    	s=g
    	v.append(p)
    	f.append(i)
    	f.sort()
    	p=0
    print(*v)