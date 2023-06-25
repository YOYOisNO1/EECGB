def program3373():
    import sys
    
    for line in sys.stdin:
        init_storage, divisor = map(int,line.split())
        produce_number = init_storage
        yes_or_no = 'No'
        for i in range(30):
            if produce_number == 0: 
                yes_or_no = 'Yes'
                break
            produce_number = produce_number * 2 % divisor
        print(yes_or_no)