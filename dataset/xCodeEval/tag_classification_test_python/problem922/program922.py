def program922():
    entrada = int(input())
    
    palavra = input()
    
    lista = []
    
    for i in xrange(entrada - 1):
        cont = 0
        teste = palavra[i] + palavra[i+1]
        for j in xrange(i+1, entrada - 1):
            if palavra[j] + palavra[j+1] == teste:
                cont += 1
        lista.append(cont)
    
    aux = max(lista)
    
    aux2 = lista.index(aux)
    
    print(palavra[aux2]) + palavra[aux2 + 1]