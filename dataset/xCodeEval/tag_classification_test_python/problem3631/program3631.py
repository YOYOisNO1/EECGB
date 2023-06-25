def program3631():
    #coding: utf-8
    
    alunos, tempo = map(int, input().split())
    
    cadeia = list(input())
    
    while tempo != 0:
    	if tempo == 0: break
    	i = 1
    	while i < len(cadeia):
    		if cadeia[i] == "G" and cadeia[i - 1] == "B":
    			cadeia[i] = "B"
    			cadeia[i - 1] = "G"
    			i += 1
     		i += 1
    	tempo-=1
    
    ans = ""
    for e in cadeia: ans += e
    
    print(ans)