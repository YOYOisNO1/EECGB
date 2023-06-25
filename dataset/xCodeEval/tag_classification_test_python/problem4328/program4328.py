def program4328():
    numbers = []
    full = ""
    
    for i in range(1,1000):
        numbers.append(i)
        full += str(numbers[i-1])
    
    n = int(input())
    
    print(full[n-1])