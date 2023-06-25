def pages():
        values = input().split(" ")
        n = int(values[0])
        p = int(values[1])
        k = int(values[2])
    
        ini = p-k
        fin = p+k
        if p-k <=0:
            ini = 1
        if p+k> n:
            fin = n
        
        pages = list(range(ini,fin+1))
    
        if 1 in pages and n in pages:
            listOfPages = map(lambda x: '('+str(p)+')' if x == p else x, pages)
            print(*listOfPages)
        elif 1 in pages:
            listOfPages = map(lambda x: '('+str(p)+')' if x == p else x, pages)
            print(*listOfPages,'>>')
        elif n in pages:
            listOfPages = map(lambda x: '('+str(p)+')' if x == p else x, pages)
            print('<<',*listOfPages)
        elif p < 1 or p > n:
            print(' ')
        else:
            listOfPages = map(lambda x: '('+str(p)+')' if x == p else x, pages)
            print('<<',*listOfPages,'>>')
    
    pages() 