def program4622():
    n,k=[int(x) for x in input().split()]
    entry=list(input())
    open_count=0
    opened=[0]*26
    closing=[-1]*26
    flag=0
    for i in range(n):
    	j=n-i-1
    	if(closing[ord(entry[j])-65]==-1):
    		closing[ord(entry[j])-65]=j
    for i in range(n):
    	if(opened[ord(entry[i])-65]==0):
    		opened[ord(entry[i])-65]=1
    		open_count=open_count+1
    	if(open_count>k):
    		flag=1
    	if(i==closing[ord(entry[i])-65]):
    		open_count=open_count-1
    if(flag==1):
    	print("YES")
    else:
    	print("NO")
    
    
    	
    	
    	
    