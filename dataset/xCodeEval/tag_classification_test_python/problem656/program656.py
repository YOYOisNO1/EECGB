def binarySearch(x,arr,l,r):
    	mid = int((l+r)/2)
    	while(l<=r):
    		if arr[mid]<x:
    			l = mid+1
    		elif arr[mid]==x:
    			return mid
    		elif arr[mid]>=x:
    			r = mid-1
    		mid = int((l+r)/2)
    		#print(l,r,mid)
    	return mid
    
    
    vert,edges = [int(x) for x in input().split()]
    if edges==0:
    	print(vert,vert)
    	exit()
    ed = int(vert/2)
    if edges>ed:
    	print(0,end=" ")
    #elif edges==ed:
    else:
    	print(vert-edges*2,end=" ")
    # else:
    # 	left = (ed-edges)*2
    # 	print(left,end=" ")
    
    x = []
    for i in range(2,vert+1):
    	x.append(int(((i)*(i-1))/2))
    #print(x)
    el = binarySearch(edges,x,0,len(x)-1)
    #print(el)
    #print(x[el])
    if x[el]==edges:
    	print(vert-el-2)
    elif edges==1:
    	print(vert-2)
    else:
    	el += 3
    	print(vert-el)