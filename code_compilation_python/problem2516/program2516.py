def program2516():
    import math
    
    line = input()
    a, b = [int(x) for x in line.split()]
    
    nice = 0
    
    for i in range (1, a*(b**2)):
        if i%b==0:
            continue
        elif (i//b)%(i%b)!=0:
            continue
        else:
            if (i//b)/(i%b)<=a and (i//b)/(i%b)>=1:
                nice+=i
        
    print nice