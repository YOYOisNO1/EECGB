def mid(ln,rn):
    	return (ln+rn)//2
    
def rfn(l,r,n,ln,rn):
    	
    	if rn<l or r<ln or n==0:
    		return 0
    	
    	if n == 1:
    		return 1
    	
    	mn = mid(ln,rn)
    
    	return rfn(l,r,n//2,ln,mn-1)+rfn(l,r,n%2,mn,mn)+rfn(l,r,n//2,mn+1,rn);
    
    if __name__ == "__main__":
    	n, l, r = map(int,input().strip().split())
    	N, total = n, 0
    
    	while N != 0:
    		total = total*2 + 1
    		N //= 2
    
    	print(rfn(l,r,n,1,total))