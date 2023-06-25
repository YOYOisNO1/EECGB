def program590():
    value = input()
    n = int(value.split()[0])
    matrix = [[0] * 2 for i in range(int(value.split()[1]))]
    total = 0
    for i in range(len(matrix)):
        value = input()
        int(value.split()[0])
        matrix[i][0] = int(value.split()[0])
        matrix[i][1] = int(value.split()[1])
    
    # defines a mini function inside the call using lambda
    # is tells the sort function to use the 2nd item to sort on it
    # rather than the 1st value (it's default value)
    matrix.sort(key=lambda x: x[1])
    
    for i in range(len(matrix)):
        if n >= matrix[-i - 1][0]:
            n -= matrix[-i - 1][0]
            total += matrix[-i - 1][0] * matrix[-i - 1][1]
            continue
        else:
            total += n * matrix[-i - 1][1]
            break
    
    print(total)