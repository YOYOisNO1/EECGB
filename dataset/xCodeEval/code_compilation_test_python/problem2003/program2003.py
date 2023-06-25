def fail():
    	print("NO")
    	exit(0)
    
    pontos = set()
    for i in range (0, 4):
    	s = list(map(int, input().split()))
    	if (s[0] != s[2] and s[1] != s[3]):
    		print("Não paralela")
    		fail()
    	pontos.add((s[0], s[1]))
    	pontos.add((s[2], s[3]))
    
    if (len(pontos) != 4):
    	fail()
    	
    
    ordenados = sorted(list(pontos))
    
    area = abs(ordenados[2][0] - ordenados[0][0]) * abs(ordenados[1][1] - ordenados[0][1])
    
    if (ordenados[0][0] == ordenados[1][0] and ordenados[0][1] == ordenados[2][1]
    and ordenados[1][1] == ordenados[3][1] and ordenados[2][0] == ordenados[3][0]
    and area > 0): 
    	print("YES")
    
    else:
    	print("NO")