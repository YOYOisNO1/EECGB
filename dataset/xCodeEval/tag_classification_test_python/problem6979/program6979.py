def program6979():
    #-------------------------------------------------------------------------------
    # Name:        module1
    # Purpose:
    #
    # Author:      asawe
    #
    # Created:     03/08/2022
    # Copyright:   (c) asawe 2022
    # Licence:     <your licence>
    #-------------------------------------------------------------------------------
    
    import sys
    
    #sys.stdin = open("C:\\Users\\asawe\\Documents\\input.txt","r")
    
    n,p = map(float,sys.stdin.readline().split())
    a = []
    for i in range(int(n)):
        b = i * (i-1) * (i-2) / n / (n-1) / (n-2)
        c = 3 * i * (i-1) * (n-i) / n / (n-1) / (n-2)
        d = 3/2 * i * (n-i-1) * (n-i) / n / (n-1) / (n-2)
        if b + c + d >= p:
            print(i)
            break