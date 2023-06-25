def program1139():
    n=int(input())
    l=list(map(int,input().strip().split()))
    i=1
    while(i<n)
    	if (l[i]<=l[i-1]):
    		break
    	else:
    		i=i+1
    while(i<n):
    	if (l[i]!=l[i-1]):
    		break
    	else:
    		i=i+1
    while(i<n):
    	if (l[i]>=l[i-1]):
    		break
    	else:
    		i=i+1
    if (i==n):
    	print ("YES")
    else:
    	print ("NO")
    
    
    