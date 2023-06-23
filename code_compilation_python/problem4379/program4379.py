def program4379():
    n = int(input()) 
    array = [1 for k in range(n+1)] 
    array[1] = 1 
    array[2] = 2 
    sumi = 3 
    for k in range(3,n+1) : 
        array[k] = 1
        c = k-1 
        while c > 0 :
            array[k] += array[c] %int(1e9 +7)
            c -= 2 
        sumi += array[k] %int(1e9 +7)
    print(sumi)