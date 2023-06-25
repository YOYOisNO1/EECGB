    n = input()
    
    
def get_result(value):
        aux = '1'
        aux_value = value[0]
        count = 0
    
        while (int(aux) <= int(aux_value)):
            current = int(aux)
            count += 1
    
            while (aux != value and len(aux) < 4):
                aux += str(current)
                count += len(aux)
    
            aux = str(current + 1)
    
        return count
    
    
    for i in range(n):
        value = input()
        print(get_result(value))