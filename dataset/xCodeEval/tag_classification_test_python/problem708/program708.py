def program708():
    from math import *
    string=input()
    #numbers = ['0','1','2','3','4','5','6','7','8','9']
    extracts=[]
    for i in range(len(string)):
    	if string[i] !='+':
    		extracts.append(int(string[i]))
    extracts.sort()
    final = []
    i = 0
    s=""
    if len(extracts)>1:
    	for x in extracts:
    		s+=str(x)
    		# print("i = ",i)
    		if i!=len(extracts)-1:
    			s+="+"
    		i+=1
    else:
    	for x in extracts:
    		s+=str(x)
    #s.join(final)
    print(s)
    