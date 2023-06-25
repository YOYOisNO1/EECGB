def program3577():
    a=map(int,input().split())
    s=input()
    b=[]
    if(a[0]>=1 and a[1]<=50):
    	for i in s:
    		b.append(i)
    	k=0
    	j = 0
    	while(k<a[1]):
    		while j < len(b)-1:
    			flag = 0
    			i = j+1
    			if(b[j]=='B' and b[i]=='G'):
    				temp=b[j]
    				b[j]=b[i]
    				b[i]=temp
    				flag = 1
    			if flag == 1:
    				j = j+2
    			else:
    				j = j+1
    			
    		k+=1
    		j = 0
    	s1=""
    	for p in range(len(b)):
    		s1=s1+b[p]
    	print(s1)