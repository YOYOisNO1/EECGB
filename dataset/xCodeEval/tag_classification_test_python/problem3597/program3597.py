def program3597():
    quant, tempo = map(int, input().split())
    fila = input()
    lista = list(fila)
    for i in range(tempo):
    	trocados = []
    	for j in range(1, len(lista)):
    		if lista[j -1] == 'B' and lista[j] == 'G' and j - 1 not in trocados:
    			lista[j], lista[j - 1] = lista[j - 1], lista[j]
    			trocados.append(j)
    saida = ''
    for e in lista:
    	saida += e
    print(saida)