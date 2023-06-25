def program2332():
    if __name__=="__main__":
    	n = input()
    	tmp = ''
    	for i in n:
    		if not len(tmp):
    			tmp = i
    		elif not i =="/":
    			tmp = tmp+i
    		elif not tmp[-1]=="/":
    			tmp = tmp+i
    	if tmp[-1]=="/"and len(tmp) not 1:
    		tmp = tmp[0:-1]
    	print(tmp)
    