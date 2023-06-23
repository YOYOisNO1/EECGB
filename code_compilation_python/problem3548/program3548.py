def program3548():
    import numpy as np
    import itertools as it
    
    n, k = [int(i) for i in input().split()]
    a = np.array([list(input()) for i in range(n)]).astype(int)
    p = np.arange(k)
    b = 10 ** p[::-1]
    print(min([np.max(np.sum(a[:, i] * b, axis=1)) - np.min(np.sum(a[:, i] * b, axis=1))
               for i in it.permutations(p)]))