def program1942():
    
    import math
    
    dim = input()
    dim = dim.split(" ")
    r = int(dim[0]) # row
    c = int(dim[1]) # column
    #row 1
    total = 1
    dist = [0 for i in range(r-1)] #row 2 to r
    
    for i in range(2, math.isqrt(r+1)+1):
        if dist[i-2] == 1:
            pass
        elif i**2 <= r: 
            dist[i-2] = 1
            counter = 1
            if i==2: 
                p=[]
                a=[]
                while i**counter <= r: 
                    a = a+[0 for i in range(c)]
                    dist[(i)**counter-2] = 1
                    for j in range(1, c+1): #row 
                        a[counter*j -1]=1
                    p.append(sum(a))
                    counter+=1 
                total +=sum(a)
            else: 
                while i**counter <= r: 
                    dist[(i)**counter-2] = 1
                    counter+=1
                total +=p[counter-2]
    
    lis = [x==0 for x in dist]
    total += sum(lis)*c
    print(total) 