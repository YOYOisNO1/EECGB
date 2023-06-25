def seg(n,l,r,lr,rg):
    	if rg<l or r<lr or n==0:
    		return 0
    	if n==1:
    		return 1
    	md=(lr+rg)//2
    	return seg(n//2,l,r,lr,md-1)+seg(n%2,l,r,md,md)+seg(n//2,l,r,md+1,rg)
    if __name__ == '__main__':
    	n,l,r=map(int,input().split())
    	tmp=n
    	cnt=0
    	while tmp!=0:
    		cnt=cnt*2+1
    		tmp//=2
    
    
    	print(seg(n,l,r,1,cnt))