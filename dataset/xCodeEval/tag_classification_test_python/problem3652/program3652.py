def program3652():
    import string
    
    inputs=map(int,input().split())
    string=list(input())
    
    while(int(inputs[1])>0):
    	i=0
    	while (i<len(string)-1):
    		if(string[i]=="B" and string[i+1]=="G"):
    			string[i+1]="B"
    			string[i]="G"
    			i+=2
    		else:
    			i+=1
    	inputs[1]-=1
    print('').join(string)		
    