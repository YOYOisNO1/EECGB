def program1825():
    not_possible = [1, 2, 4, 5, 8, 11]
    
    n_tests = int(input())
    
    for i in range(n_tests):
        number = int(input())
        if number in not_possible:
            print('NO')
        else:
            print('YES')
            