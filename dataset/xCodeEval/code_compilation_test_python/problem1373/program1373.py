    x = int(input())
    
    
def is_power_of_two(x):
        return x & (x - 1) == 0
        
        
def lowest_power_of_two(x):
        return 1 << (x.bit_length() - 2)
    
    
    if is_power_of_two(x):
        return 1
    else:
        return x - lowest_power_of_two(x)