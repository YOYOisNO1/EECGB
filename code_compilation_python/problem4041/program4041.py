def program4041():
    s=input()
    ans=0
    for i in range(0,len(s)):
    	if(s[i]>'a' and s[i]<'z'):
    		ans-=ord(s[i])-ord('a')+1
    	else:
    		ans+=ord(s[i])-ord('A')+1
    print ans