    for i in range(4):
    	st = input()
    	lista[i] = st.split(" ")
    
    print(lista)
def ff(n):
    	if n ==0 :
    		return 3
    	if n%2==0:
    		return n+1
    	else:
    		return n-1
    
def rec(lista):
    	for i in range(len(lista)):
    		for j in range(len(lista[i])):
    			if lista[i][3] == lista[i][j] == 1:
    			   print("YES")
                    break
    			if lista[i][j] == lista[ff(j)][3] == '1' :
    				print("YES")
    				break
    
    
    rec(lista)