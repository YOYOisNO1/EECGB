def program3696():
    #
    #   507A. Amr and Music
    #
    
    no_of_instruments, days = map(int, input().split())
    instruments = list(map(int, input().split()))
    indicies = [i for i in range(1, no_of_instruments + 1)]
    a = sorted(zip(instruments, indicies))
    has_solution = False
    result = []
    for day, index in a:
        if day <= days:
            days -= day
            has_solution = True
            result.append(index)
    if not has_solution:
    	print(0)
    else:
        print(len(result))
        print(' ').join(map(str, sorted(result)))