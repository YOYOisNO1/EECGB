def program4243():
    n=str(input())
    s=''
    for i in range(len(n)):
    	if(n[i]=='1' or n[2]=='2'):
    		s=s+'.'
    	elif(n[i]=='3' or n[i]=='7'):
    		s=s+n[i]
    	elif(n[i]=='4'):
    		s=s+'6'
    	elif(n[i]=='6'):
    		s=s+'6'
    	elif(n[i]=='5'):
    		s=s+'9'
    	elif(n[i]=='9'):
    		s=s+'9'
    	elif(n[i]=='0'):
    		s=s+'8'
    	elif(n[i]=='8'):
    		s=s+'8'
    j=len(s)-1
    k=0
    for i in range(len(s)):
    	if(s[i]=='.'):
    		k=1
    		break
    	elif(s[i]!=s[j]):
    		k=1
    		break
    	else:
    		pass
    	j-=1
    if(k==1):
    	print("No")
    else:
    	print("Yes")