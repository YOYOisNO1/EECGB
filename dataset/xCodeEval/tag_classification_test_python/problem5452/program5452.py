    # http://codeforces.com/problemset/problem/322/B
    
def divide3(lista):
    	total = 0
    	for i in lista:
    		total += int(i / 3)
    	
    	return total
    
def tiralista(lista, valor):
    	tmp = lista[:]
    	for i in range(len(tmp)):
    		if tmp[i] == 0:
    			return lista, 0
    		tmp[i] -= valor
    	return tmp, valor
    
    lista = map(int, input().split())
    nums = []
    for i in range(3):
    	tmp, total = tiralista(lista, i)
    	total += divide3(tmp)
    	nums.append(total)
    	
    print(max(nums))