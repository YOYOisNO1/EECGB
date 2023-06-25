def program2899():
    input()
    X = list(map(int, input().split()))
    Arith = [X[i] - X[i + 1] for i in range(len(X) - 1)]
    print(X[-1] - Arith[0] if Arith.count(Arith[0]) == len(Arith) else X[-1])
    
    # UB_CodeForces
    # Advice: Do what you can with what you have and never be satisfied
    # Location: Still next to the tissue box
    # Caption: Sb had wet dream again