    from math import *
    # from sys import stdin,stdout
    
def binarySearch(arr,x,i):
    	l=i
    	r=len(arr)-1 
    	while l <= r: 
    		mid = (l + r)//2; 
    		if arr[mid] == x: 
    			return mid 
    		elif arr[mid] < x: 
    			l = mid + 1
    		else: 
    			r = mid - 1
    	return -1
    
def js(arr,x):
    	l=0
    	r=len(arr)-1
    	ans=-1
    	while(l<=r):
    		m=(l+r)//2
    		if(arr[m]<=x):
    			ans=m
    			l=m+1
    		else:
    			r=m-1
    	return ans
    
def jg(arr,x):
    	l=0
    	r=len(arr)-1
    	ans=-1
    	while(l<=r):
    		m=(l+r)//2
    		if(arr[m]>=x):
    			ans=m
    			r=m-1
    		else:
    			l=m+1
    	return ans
    
# def ceil(a,b):
    # 	if a%b == 0:
    # 		return int(a/b)
    # 	else:
    # 		return (a//b + 1)
    
    # from collections import deque
    
    # n,m,k=map(int,input().split())
    # ar=list(map(int,input().split()))
    
    # q=[]
    # sm=[0]*(m+1)
    # for i in range(m+1):
    # 	queue = deque()
    # 	q.append(queue)
    
    
    # ans=1
    # for i in range(m+1)
    # 	q[ar[i]].append(i)
    # 	if(len(sm[ar[i]])==0):
    # 		sm[ar[i]].append(1)
    # 	else:
    
    # 	while q[ar[i]]:
    
    
    n=int(input())
    s=list(input())
    a="zyxwvutsrqponmlkjihgfedcb"
    count=0
    for i in range(25):
    	for j in range(n):
    		if(s[j]==a[i]):
    			x=j-1
    			y=j+1
    			while(x>=0):
    				if(s[x]==-1 or s[x]==a[i]):
    					x-=1
    				elif(s[x]==chr(ord(s[j])-1)):
    					break
    				else:
    					break
    			while(y<n):
    				if(s[y]==-1 or s[y]==a[i]):
    					y+=1
    				elif(s[y]==chr(ord(s[j])-1)):
    					break
    				else:
    					break
    			# print(x,y,s[j],s)
    			if((x>=0 and s[x]!=-1 and s[x]==chr(ord(s[j])-1)) or (y<n and s[y]!=-1 and s[y]==chr(ord(s[j])-1))):
    				count+=1
    				s[j]=-1
    print(count)