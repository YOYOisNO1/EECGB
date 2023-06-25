def program4838():
    """import sys
    sys.stdin=open("input.in","r")
    sys.stdout=open("output.out","w")"""
    
    x=int(input())
    l=[]
    s=0
    for i in range(x):
    	l.append(input().split())
    for i in range(x):
    	for j in range(x):
    		if i==j:
    			s+=int(l[i][j])
    		elif i==x-(j+1):
    			s+=int(l[i][j])	
    		elif i==int(x/2):
    			s+=int(l[i][j])
    		elif j==int(x/2):
    			s+=int(l[i][j])	
    print(s)	