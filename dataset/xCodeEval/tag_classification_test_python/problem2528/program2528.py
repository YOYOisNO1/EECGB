def program2528():
    dict1 = {}
    a = 0
    x = [int(x) for x in input().split()]
    
    for i in range(4):
        dict1[x[i]] = None
    
    for i in range(4):
        if dict1[x[i]] != None:
            dict1[x[i]] = dict1[x[i]] + 1
            a = a + 1
        else:
            dict1[x[i]] = 1
    
    
    print(a)