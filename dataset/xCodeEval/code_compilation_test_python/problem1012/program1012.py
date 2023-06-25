def program1012():
    año = input()
    acumulador = 0
    i = 1
    while(i < len(año)-1):
    	ultimo = int(año[-i])
    	acumulador += (10 - ultimo)*10**i
    	año = str(int(año)+acumulador)
    	i+=1
    
    print(acumulador)