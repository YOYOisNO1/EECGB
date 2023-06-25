def program1486():
    #coding: utf-8
     
    nome = input()
    vogais = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    final = ''
    for i in nome:
    	if i not in vogais:
    		final += '.'
    		final += i.lower()
     
     
    print("%s") % final