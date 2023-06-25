def program709():
    # Getting input
    entry = input()
    
    # Splitting the entry with the '+',
    # sorting numbers and adding '+' sign
    numbers = entry.split('+')
    numbers.sort()
    numbers = list('+'.join(numbers))
    
    # Printing final result
    result = ''.join(numbers)
    print(result)