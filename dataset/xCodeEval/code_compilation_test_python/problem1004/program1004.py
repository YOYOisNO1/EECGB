def program1004():
    X = list(map(int, input().split())
    print(str(X[0]) + '0 ' + str(X[0]) + "1" if X[0] == X[1] else (
        str(X[0]) + '9 ' + str(X[1]) + "0" if X[1] - X[0] == 1 else ("9 10" if X[1] - X[0] == 8 else -1)))
    
    # UB_CodeForces
    # Advice: Falling down is an accident, staying down is a choice
    # Location: Mashhad for few days
    # Caption: Finally happened what should be happened
    # CodeNumber: 685