    n, k, x = map(int, input().split())
    
    balls = list(map(int, input().split()))
    
def conta_pares(balls1, num):
        pares = []
        for w in range(n-1):
            if balls1[w] == balls1[w+1] == num:
                pares.append(w)
                pares.append(w+1)
        return pares
    
    
    
    if n < 2:
    	print(0)
    	exit()
    lista_pares = conta_pares(balls, x)
    
    if lista_pares == []:
    	print(0)
    	exit()
    
    par = False
    maximo = 2
    
    for i in range(0, len(lista_pares)-1, 2):
      il, ir = lista_pares[i], lista_pares[i+1]
      pontos = 2
      while True:
        
        if il>0 and ir < n-1 and balls[il-1] == balls[ir+1]:
              if il-2 >= 0 and balls[il-2] == balls[il-1]:
                  pontos += 3
                  il -= 2
                  if ir+2 < n and balls[ir+2] == balls[ir+1]:
                      pontos += 1
                      ir += 2
                  else:
                    ir += 1
              elif ir+2 < n and balls[ir+2] == balls[ir+1]:
                  pontos += 3
                  ir += 2
                  il -= 1
              else:
                  if pontos > maximo:
                    maximo = pontos
                  print(pontos)
                  break
        else:
              if pontos > maximo:
                  maximo = pontos
              break
    
    print(maximo)
    