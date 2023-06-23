def program1943():
    dim = input()
    dim = dim.split(" ")
    r = int(dim[0]) # row
    c = int(dim[1]) # column
    
    total = 1
    dist = [0 for i in range(r-1)] #row 2 to r
    
    p=[0 for i in range(int((r+1)**.5) +1)]
    a=[]
    counter = 1
    for i in range(1, 20):
        a = a+[0 for i in range(c)]
        for j in range(1, c+1): #row 
            if a[i*j -1]==0: 
                p[i-1]+=1
            a[i*j -1]=1 
    a.clear()
    z=[sum(p[0:i]) for i in range(1,len(p))]
    #print(z)
    
    for i in range(2, (r+1)):
        if dist[i-2] == 1:
            pass
        else: 
            dist[i-2] = 1
            counter = 1
            while i**counter <= r: 
                dist[(i)**counter-2] = 1
                counter+=1 
            total += z[counter-2]
            #print(i, counter, z[counter-2])
            
    print(total) 