def program3858():
    # import sys
    # sys.stdin=open("input.in","r")
    # sys.stdout=open("output.out","w")
    n=int(input())
    a=input()
    s=list(a)
    sg=[]
    i=0
    while i<n:
    	if s[i]=='B':
    		size=1
    		j=i+1
    		if j<n:
    			while j<n and s[j]!='W':
    				size+=1
    				j+=1
    		sg.append(size)
    		i+=size
    	else:
    		i+=1		
    print(len(sg))
    print(*sg)			