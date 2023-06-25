    import sys 
    import math
    
def IO():
    	sys.stdin=open("pyinput.txt", 'r')
    	sys.stdout=open("pyoutput.txt", 'w')
    
def GCD(a, b):
    	if(b==0): return a
    	else: return GCD(b, a%b)
    
def LCM(a, b): return a*(b//GCD(a, b))
    
def scan(TYPE_1, TYPE_2=0):
    	if(TYPE_1==int):
    		return map(int, sys.stdin.readline().strip().split())
    	elif(TYPE_1==float):
    		return map(float, sys.stdin.readline().strip().split())
    	elif(TYPE_1==list and TYPE_2==float):
    		return list(map(float, sys.stdin.readline().strip().split()))
    	elif(TYPE_1==list and TYPE_2==int):
    		return list(map(int, sys.stdin.readline().strip().split()))
    	elif(TYPE_1==str):
    		return sys.stdin.readline().strip()
    	else: print("ERROR!!!!") 
    
    
    
def main():
    	
    	n, k=scan(int)
    	a=scan(list, int)
    
    	idx=[]
    	for i in range(n):
    		idx.append((a[i], i))
    
    	idx.sort()
    	ans=[(i+1)//2 for i in a]
    
    	x=sum(ans)
    	if(x>k):
    		print(-1)
    		return
    	k-=x
    
    	i=n-1
    	while(k>0):
    		x=idx[i][1]
    		inc=min(a[x]-ans[x], k)
    		ans[x]+=inc
    		k-=inc
    		i-=1
    
    	print(*ans)
    	
    
    # IO()
    main()