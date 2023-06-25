def program1213():
    s=input()
    cnt=0
    gk=s.replace("at", "@")
    gk=gk.replace("dot", ".")
    #print(gk)
    n=len(gk)
    k=list(gk)
    if(k[0]=='.'):
    	k[0]="dot"
    if(k[n-1]=='.'):
    	k[n-1]="dot"
    if(k[0]=='@'):
    	k[0]="at"
    if(k[n-1]=='@'):
    	k[n-1]="at"
    #s=string(k)
    for x in range(len(k)):
    	if(k[x]=="@" and cnt==0):
    		cnt=1
    	elif(k[x]=="@"):
    		k[x]="at"	
    
    	print(k[x],end="")
    #print(k)	
    
    #//print(len(gk))