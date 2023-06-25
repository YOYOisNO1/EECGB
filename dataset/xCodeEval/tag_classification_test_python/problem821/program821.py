def program821():
    n = int(input())
    colors = 'ROYGBIV'
    eggs = [colors[i % 7] for i in xrange(n)]
    
    if(eggs[-1] == 'Y'):
        eggs[-1] = 'G'
        eggs[-2] = 'B'
        eggs[-3] = 'Y'
    if(eggs[-1] == 'O'):
        eggs[-2] = 'Y'
        eggs[-1] = 'G'
    if(eggs[-1] == 'R'):
        eggs[-1] = 'G'
        
    print('').join(eggs)