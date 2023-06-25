    import math
    
def is_square(n):
        sqrt = math.sqrt(n)
        return (sqrt - int(sqrt)) == 0
    
     
    pixel = int(input())
    
    
    if is_square(pixel): result = (int(math.sqrt(self.pixel)),int(math.sqrt(self.pixel)))
    else:
        lista =[]
        for i in range(1, pixel+1):
            if pixel%i == 0 :lista.append(i)
        pivot = int(len(lista)/2)-1
        row = lista[pivot]
        column = lista[pivot+1]
        result = (row,column)
    
     priint(f"{' '.join(map(str,result))}")