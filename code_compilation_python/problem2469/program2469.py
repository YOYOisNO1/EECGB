def program2469():
    n,m=map(int,input().split())
    r=[]
    b=[]
    turn=1
    s=[]
    vas=0
    pet=0
    for i in range(n):
    	r.append("r")
    for i in range(m):
    	b.append("b")
    for i in range(n+m):
    	if turn==0:
    		if s[i-1]=="b" and len(r)>0:
    			s.append("r")
    			r=r[1:]
    
    		elif s[i-1]=="r" and len(b)>0:
    			s.append("b")
    			b=b[1:]
    		elif len(b)>0:
    			s.append("b")
    			b=b[1:]		 
    		else:
    			s.append("r")
    			r=r[1:]
    		turn+=1
    	else:
    		if i==0:
    			s.append("b")
    			b=b[1:]
    		else:		
    			if s[i-1]=="r" and len(r)>0:
    				s.append("r")
    				r=r[1:]
    
    			elif s[i-1]=="b" and len(b)>0:
    				s.append("b")
    				b=b[1:]
    			elif len(b)>0:
    				s.append("b")
    				b=b[1:]		 
    			else:
    				s.append("r")
    				r=r[1:]
    		turn-=1
    s=''.join(s)
    # print s
    s_back=s
    while s.count('rr')>0:
    	vas+=s.count('rr')
    	s=s.replace('rr','r')
    	# print s,vas
    while s.count('bb')>0:
    	vas+=s.count('bb')
    	s=s.replace('bb','b')
    	# print s,vas
    # print s_back
    pet+=s_back.count('br')
    pet+=s_back.count('rb')
    a1=[vas,pet]
    # print a1
    s=[]
    r=[]
    b=[]
    turn=1
    vas=0
    pet=0
    for i in range(n):
    	r.append("r")
    for i in range(m):
    	b.append("b")
    for i in range(n+m):
    	if turn==0:
    		if s[i-1]=="b" and len(r)>0:
    			s.append("r")
    			r=r[1:]
    
    		elif s[i-1]=="r" and len(b)>0:
    			s.append("b")
    			b=b[1:]
    		elif len(b)>0:
    			s.append("b")
    			b=b[1:]		 
    		else:
    			s.append("r")
    			r=r[1:]
    		turn+=1
    	else:
    		if i==0:
    			s.append("r")
    			r=r[1:]
    		else:		
    			if s[i-1]=="r" and len(r)>0:
    				s.append("r")
    				r=r[1:]
    
    			elif s[i-1]=="b" and len(b)>0:
    				s.append("b")
    				b=b[1:]
    			elif len(b)>0:
    				s.append("b")
    				b=b[1:]		 
    			else:
    				s.append("r")
    				r=r[1:]
    		turn-=1
    s=''.join(s)
    # print s
    s_back=s
    while s.count('rr')>0:
    	vas+=s.count('rr')
    	s=s.replace('rr','r')
    	# print s,vas
    while s.count('bb')>0:
    	vas+=s.count('bb')
    	s=s.replace('bb','b')
    	# print s,vas
    # print s_back
    pet+=s_back.count('br')
    pet+=s_back.count('rb')
    a2=[vas,pet]
    for i in max(a1,a2):
    	print i,