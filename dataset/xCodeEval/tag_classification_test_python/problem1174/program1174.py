def program1174():
    posiciones = input()
    tiempo = int(input())
    posiciones = posiciones.split(' ')
    inicio = posiciones[0]
    final = posiciones[1]
    
    dict = ['^','>','v','<']
    
    
    if tiempo >4:
        tiempo =tiempo%4
    
    #contando ccw
    contador_izq = dict.index(inicio) 
    for n in range(tiempo):
        if contador_izq-1 <0:
            contador_izq= 3
        else:
            contador_izq -=1
    
    #contando cw
    contador_der = dict.index(inicio)  
    for n in range(tiempo):
        if contador_der+1 >3:
            contador_der= 0
        else:
            contador_der +=1
    
    
    
    if (posiciones[1] == dict[contador_izq]) and (posiciones[1] != dict[contador_der]):
        print('ccw')
    elif (posiciones[1] != dict[contador_izq]) and (posiciones[1] == dict[contador_der]):
        print('cw')
    else: 
        print('undefined')