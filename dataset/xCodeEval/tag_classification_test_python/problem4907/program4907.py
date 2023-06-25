def program4907():
    n = int(input())
    x = [int(i) for i in input().split()]
    
    chest = 0
    bicep = 0
    back = 0
    
    for i in range(n):
        if i%3 == 0:
            chest += x[i]
        elif i%3 == 1:
            bicep+= x[i]
        elif i%3 == 2:
            back += x[i]
    
    y = [chest,bicep, back]
    m = max(y)
    
    '''
    if( m == chest):
        print("chest")
    elif m == bicep:
        print("bicep")
    elif m == back:
        print("back")
    '''
    
    if(chest>bicep and chest>back):
    	    print("chest");
    elif(bicep>chest and bicep>back):
    	    print("biceps");
    else:
    	    print("back");