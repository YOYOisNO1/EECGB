def solucionar(x, y): 
        if x > y: 
            yx = y
            xy=pow(x, (y/x))
            if (yx>xy): 
                return '<'
            elif yx==xy:
                return '='
            else:
                return '>'
               
        elif x == y: 
            return '='
        
        else:
            xy=x
            yx=pow(y, (x/y))
            if yx > xy:
                return '<'
            elif yx == xy:
                return '='
            else:
                return '>'         
            
    
    if __name__ == '__main__':
        x, y = [int(s) for s in input().split(" ")]
        solucion = solucionar(x, y)
        print(solucion)