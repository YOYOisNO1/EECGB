def program3503():
     k = map(int, input().split())
    
    print(['Yes', 'No'][any((n + 1) % d
                            for d in range(2, k + 1))])
    
    