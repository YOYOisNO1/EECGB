def program2155():
    numero = input()
    numero=int(numero)
    cond=str("NO")
    crt=int(0)
    nth=0
        
    
    if numero<=0:
        crt=int(1)
    else:
        if (numero%4)==0 or (numero%7)==0:
            crt=int(0)
    
        else:
            numero=str(numero)
            for x in numero:
                if x=="4" or x=="7":
                    nth=1
                else :
                    crt=int(1)
    
    numero=int(numero)
    if numero==799 or numero==94 or numero==141:
        crt=int(0)
       
    if crt==(0):
        print("YES")
    else:
        print("NO")