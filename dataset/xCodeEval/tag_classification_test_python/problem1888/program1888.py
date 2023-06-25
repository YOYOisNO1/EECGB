def program1888():
    a=input().split(' ')
    a=map(int, a)
    
    if a[1]<=int((a[0]+1)/2):
    	j=2*(a[1])-1
    	print(j)
    else:
    	k=2*(a[1]-int((a[0]+1)/2))
    	print(k)