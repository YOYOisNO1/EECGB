def program3504():
    n, k = map(int, input().split())
    
    lista = [0]*100000
    
    flag = True
    if k > 1000000: k = 100000
    for i in range(1, k+1):
        lista[n%i] += 1
        if lista[n%i] > 1: 
             print "No"
            flag = False
            break
    
    if flag: print "Yes"