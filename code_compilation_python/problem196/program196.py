def program196():
    n,k=[*map(int,input().split())]
    st=sorted(input())
    li=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    newli=[]
    for i in st:
    	newli.append(li.index(i)+1)
    if k==1:
    	print(newli[0])
    	quit()
    newli1=[]
    for i in range(len(newli)-1):
    	newli1.append(newli[i+1]-newli[i])
    if sum(newli1)<=k-1:
    	print(-1)
    	quit()
    else:
    	addvalue=newli[0]
    	addtime=1
    	cursor1=0
    	cursor2=1
    	while addtime<k:
    		try:
    			newli[cursor2]-newli[cursor1]<=1
    		except:
    			while 1==1:
    				a=1
    				b=2
    				c=a+b
    		if newli[cursor2]-newli[cursor1]<=1:
    			cursor2+=1
    		else:
    			addvalue+=newli[cursor2]
    			cursor1=cursor2
    			cursor2+=1
    			addtime+=1
    	print(addvalue)	