def program3614():
    n,t=map(int,input().split())
    x=input("")
    y=len(x)
    z=[]
    for c in range(n):
    	z.append(x[c])
    if t > 1:
    	for count in range(t):
    		
    		pos=0
    		while (pos<y-1):
    			if (x[pos]=="B" and x[pos+1]=="G"):
    				z[pos]="G"
    				z[pos+1]="B"
    			pos+=1
    		x=''.join(map(str,z))
    		#print(x)
    		#print(z)
    		
    		
    		
    if t==1:
    		pos=0
    		while (pos<y-1):
    			if (x[pos]=="B" and x[pos+1]=="G"):
    				z[pos]="G"
    				z[pos+1]="B"
    			pos+=1
    
    x=''
    x=x.join(map(str,z))
    print(x)
    
    