def main():
    	palabra = input("")
    	wordlist = list (palabra)
    	for x in range (len(wordlist)):
    		anteriorEstado = wordlist[x-1]
    		letra = wordlist[x]
    		if vocales(anteriorEstado) == False and vocales(letra) == False and anteriorEstado != "n":
    			print(("NO"))
    			return
    		if x == len(wordlist)-1 and vocales(letra)==False and letra != "n":
    			print(("NO"))
    			return
    	print(("Yes"))
    
    
def vocales(letra):
    	return letra in ["a", "e", "i", "o","u"]
    
    main()
    #