def program245():
    num = int(input())
    lista = map(int, input().split())
    
    resp = 1
    um = False
    cont = 0
    
    for i in lista:
        if um: cont += 1
    
        if i == 1 and um:
            resp *= cont
            cont = 0
    
        if i == 1: 
            um = True
            
    if not um: resp = 0
    print(resp)