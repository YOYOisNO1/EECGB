def program1949():
    n=int(input())
    s=input()
    s1=""
    for i in range(0,s.__len__()):
    	if s[i]=='0' or s[i]=='1':
    		continue
    	if s[i]!='4' and s[i]!='6' and s[i]!='8' and s[i]!='9':
    		s1=s1+s[i]
    	else:
    		if s[i]=='4':
    			s1=s1+'223'
    		elif s[i]=='6':
    			s1=s1+'53'
    		elif s[i]=='8':
    			s1=s1+'2227'
    		else:
    			s1=s1+'3327'
    l=[]
    for x in range(0,s1.__len__()):
    	l.append(s1[x])
    l.sort()
    l.reverse()
    for x in l:
    	print(x,end="")
    print()