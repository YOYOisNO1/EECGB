def int_to_3(a):
    	string = "";
    	while(a>0):
    		string+=str(a%3)
    		a/=3;
    	string = list(string)
    	string.reverse()
    	string ="".join(string)
    	return string
    
def add_zero(s,n):
    	if(n<=0):
    		return s
    	before = ['0']*n
    	for x in s:
    		before.append(x)
    	return "".join(before)
    
    #print(int_to_3(14))
    a,c = [int(x) for x in input().split(' ')]
    a3 = int_to_3(a)
    c3 = int_to_3(c)
    #print(a3,c3,)
    max_len = max(len(a3),len(c3))
    a3 = add_zero(a3,max_len-len(a3))
    c3 = add_zero(c3,max_len-len(c3))
    #print(a3,c3)
    b = []
    for i in range(max_len):	
    	new = (int(c3[i])-int(a3[i]))
    	if(new<0):
    		new+=3;
    	b.append(str(new))
    b3 = "".join(b)
    if(not b3):
    	b3="0"
    print(int(b3,3))
    	
    
    