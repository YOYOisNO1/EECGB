def program1234():
    import math
    
    n=int(input())
    L=list(map(int,input().split()))
    L.sort()
    dict={}
    dict[L[0]]=1
    for i in range(1,len(L)):
    	if(L[i]!=L[i-1]):
    		dict[L[i]]=1
    	else:
    		dict[L[i]]+=1
    
    maxi=1
    for e in dict.keys():
    	if(dict[e]==2 and e>maxi):
    		maxi=e
    
    M=list(dict.keys())
    N=[0]*len(M)
    for i in range(0,len(M)):
    	for j in range(0,len(M)):
    		if(M[i]%M[j]==0):
    			N[i]+=1
    
    for i in range(0,len(N)):
    	for j in range(0,i+1):
    		if(N[i]+N[j]==n and math.gcd(M[i],M[j])==maxi):
    			print(str(M[i])+" "+str(M[j]))
    			break
    
    
    
    
    
    