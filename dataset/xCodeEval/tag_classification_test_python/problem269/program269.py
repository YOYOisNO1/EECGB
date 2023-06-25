def program269():
    a=input()
    l=a.split(' ')
    s=l[0][0]
    for i in l[0][1:]:
    	if i<l[1][0]:
    		s=s+i
    	else:
    		break
    s=s+l[1][0]
    print(s)