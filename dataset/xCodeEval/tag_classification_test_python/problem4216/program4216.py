def program4216():
    if __name__ == "__main__":
    	s = input()
    	flag = 1
    	bag = "CODEFORCES"
    	if bag in s:
    		rem = s[:s.index(bag)]+ s[s.rindex(bag)+len(bag):]
    		k=[]
    		st = 0
    		for i in s:
    			if i==bag[st]:
    				st+=1
    			else:
    				break
    			if st == 10:
    				break
    		rem2 = bag[st:]
    		if s.rindex(rem2)+len(rem2)==len(s):
    			print("YES")
    		elif rem==bag:
    			print("YES")
    		elif s.index(bag)>0 and s.rindex(bag)+len(bag)<len(s):
    			print("NO")
    		else:
    			print("YES")
    		exit()
    	k = []
    	for i in bag:
    		x = "".join(k)
    		if x in s:
    			k.append(i)
    		else:
    			k.pop()
    			x = "".join(k)
    			break
    
    	rem = bag[bag.index(x)+len(x):]
    	if rem in s :
    		if s.index(x)==0 and s.rindex(rem)+len(rem)==len(s):
    			print("YES")
    		else:
    			print("NO")
    	else:
    		print("NO")