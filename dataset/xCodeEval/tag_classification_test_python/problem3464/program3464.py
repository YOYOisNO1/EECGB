def program3464():
    input()
    X, i = input(), 0
    while i < len(X):
        Temp = X[i:i + 3]
        if Temp == 'ogo':
            while Temp == 'ogo':
                i += 2
                Temp = X[i:i + 3]
            print("***", end="")
        else:
            print(X[i], end="")
        i += 1