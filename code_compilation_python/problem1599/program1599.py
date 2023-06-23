def program1599():
    n=int(input())
    if n>0:
    	print(n)
    else:
    	if n<0:
    		x=str(n)
    		j=len(x)
    		r=x[j-1]
    		s=x[j-2]
    		if r>s:
    			t=''
    			for u in range (0,j,1):
    				if x[u]!=r:
    					t=t+x[u]
    			t=int(t)
    			print(t)
    		else:
    			if s>r:
    				t=''
    				for u in range (0,j,1):
    					if x[u]!=s:
    						t=t+x[u]
    				if t[1]=="0":
    					print("0")
    				else:
    					t=int(t)
    					print(t)
    	else:
    		if n==0:
    			print(n