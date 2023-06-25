def program1013():
    anno = input()
    if(int(anno) <= 9) print(1)
    else:
    	acumulador = 0
    	i = 1
    	while(i < len(anno)):
    		ultimo = int(anno[-i])
    		acumulador += (10 - ultimo)*10**(i-1)
    		anno = str(int(anno)+acumulador)
    		i+=1
    
    	print(acumulador)