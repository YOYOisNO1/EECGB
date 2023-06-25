def program335():
    
    d={0:[1,2,3,4,5,6],1:[2,3],2:[1,2,7,5,4],3:[1,2,7,3,4],4:[6,7,2,3],5:[1,6,7,3,4],6:[1,6,5,4,3,7],7:[1,2,3,4],8:[1,2,3,4,5,6,7,8],9:[1,2,3,4,6,7]}
    
    n=int(input())
    a=n%10
    b=n//10
    #print(a,b)
    s=set(d[a])
    s1=set(d[b])
    count=0
    count1=0
    #print(s,s1)
    for i in range(0,10):
    	x=set(d[i])
    	y=s.difference(x)
    	if(len(y)==0):
    		count=count+1
    
    for i in range(0,10):
    	x=set(d[i])
    	y=s1.difference(x)
    	if(len(y)==0):
    		count1=count1+1
    
    print(count*count1)