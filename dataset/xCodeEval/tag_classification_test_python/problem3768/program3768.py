def program3768():
    a=input()
    dead=False
    semidead=False
    fr=0
    ind=None
    d=0
    for i in range(len(a)//2):
    	if a[i-min(fr,0)]!=a[-i-1-max(fr,0)]:
    		if d==0:
    			if a[i]==a[-i-2]:
    				fr=1
    				ind=i
    				d+=1
    			elif a[i+1]==a[-i-1]:
    				fr=-1
    				ind=len(a)-i-1
    				d+=1
    			else:
    				dead=True
    				print('NA')
    				break
    		else:
    			semidead=True
    			break
    if semidead:
    	d=0
    	fr=0
    	for i in range(len(a)//2):
    		if a[i-min(fr,0)]!=a[-i-1-max(fr,0)]:
    			if d==0:
    				if a[i]==a[-i-2]:
    					if fr!=-1:
    						if a[i+1]==a[-i-1]:
    							fr=-1
    							ind=len(a)-i-1
    							d+=1
    						else:
    							dead=True
    							print('NA')
    							break
    					else:
    						ind=i
    						d+=1
    				elif a[i+1]==a[-i-1]:
    					if fr!=1:
    						dead=True
    						print('NA')
    						break
    					ind=len(a)-i-1
    					d+=1
    				else:
    					dead=True
    					print('NA')
    					break
    			else:
    				dead=True
    				print('NA')
    				break
    if not dead:
    	if d==0:
    		print(a[0:len(a)//2],a[len(a)//2],a[len(a)//2::],sep='')
    	elif fr==1:
    		print(a[0:ind],a[-1-ind],a[ind::],sep='')
    	else:
    		print(a[0:ind+1],a[len(a)-1-ind],a[ind+1::],sep='')