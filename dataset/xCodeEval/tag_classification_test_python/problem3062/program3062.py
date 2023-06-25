def program3062():
    x = map(lambda n: int(n), input().split(" "))
    
    
    dif = x[0]**2 + x[2]**2 + x[4]**2
    area = (x[5] + x[0] + x[4])**2
    print(area) - dif