    import math
    lista = []
def divisors(x):
        for i in range(1,int(math.sqrt(x))+1):
            if x%i == 0:
                lista.append(i)
                lista.append(x/i)
        lista.sort()
        lista.reverse()
    
        for j in range(len(lista)):
            k = ''
            a = -1
            b = 0
            k = str(bin(lista[j]))
            print k
            for v in range(len(k)):
                if k[v] == '0':
                    a += 1
                if k[v] == '1':
                    if a>0:
                        a = 0 
                        b = 0
                        break
                    else:
                        b+=1
                    
            if b-a == 1: return lista[j]
                
       
    x = int(input())
    k = divisors(x)
    print (k)
    # 1512531319532