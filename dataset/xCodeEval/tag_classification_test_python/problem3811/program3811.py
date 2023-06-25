def swap_n_sort(X, i, j):
        X = X[0:i] + X[j] + X[i+1:j] + X[i] + X[j+1:]
        X = X[:i+1] + ''.join(reversed(sorted(X[i+1:])))
        return X
    
    X = ''.join(reversed(sorted(input())))
    Y = input()
    
    if len(X) < len(Y):
        print(X)
    else:
        eq = True
        i = 0
        while i < len(X):
            if int(''.join(X)) < int(''.join(Y)): break
            x = int(X[i])
            y = int(Y[i])
            if x < y:
                break
            if x == y and eq == True:
                i += 1
            if x > y or (x == y and eq == False):
                nx = -1
                nj = -1
                for j in range(i+1, len(X)):
                    xx = int(X[j])
                    if ((xx <= y and eq == True) or (xx < y and eq == False)) and xx > nx: 
                        nj = j
                        nx = int(X[j])
                if nx > -1:
                    X = swap_n_sort(X, i, nj)
                    i += 1
                else:
                    i -= 1
                    eq = False
                    
        print(X)