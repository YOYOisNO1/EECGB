def program293():
    # your code goes here
    str = input()
    str = str.split(' ')
    t = int(str[0])
    s = int(str[1])
    x = int(str[2])
    
    flag=0
    if x==t:
    	flag=1	
    elif x<t:
    	flag=2
    else:
    	if (x-t)%s==0:
    		flag=1
    	elif (x-t-1)%s==0 and (x-t-1)!=0:
    		flag=1
    	else:
    		flag=2
    if flag==1:
    	print('YES')
    else:
    	print('NO')