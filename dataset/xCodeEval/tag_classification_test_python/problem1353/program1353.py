def program1353():
    # Aluno: Thiago Santos de Moura - 116210967
    
    entradas = map(int, input().split())
    valores_casas = map(int, input().split())
    
    num_casas = entradas[0]
    index_love = entradas[1] - 1
    money = entradas[2]
    metros = 10
    max_length = num_casas * metros
    result = max_length
    i = 1
    
    while(True):
      before = index_love - i
      after = index_love + i
      if((before < 0 and after >= num_casas) or result != max_length):
        break
      elif(before >= 0 and valores_casas[before] !=0 and valores_casas[before] <= money):
        if(result > (i*metros)):
          result = (i*metros)
      elif(after < num_casas and valores_casas[after] <= money and valores_casas[after] !=0):
        if(result > (i*metros)):
          result = (i*metros)
      i+=1
    
    print(result)