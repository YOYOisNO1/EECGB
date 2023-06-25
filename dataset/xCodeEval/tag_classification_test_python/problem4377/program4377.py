def program4377():
    s=input()
    at=s.find('at',1)
    s=s[:at]+'@'+s[at+2:]
    pos=1
    while 1:
    	ns=''
    	dot=s.find('dot',pos,-1)
    	if dot==-1:
    		break
    	ns+=s[:dot]
    	ns+='.'
    	pos=dot+1
    	ns+=s[dot+3:]
    	s=ns
    print(s)