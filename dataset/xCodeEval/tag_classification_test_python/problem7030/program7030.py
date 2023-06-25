def program7030():
    import sys
    n = int(sys.stdin.readline())
    
    L = [0, 1]
    for i in range (1, 48):
        L.append(2 * L[i] + 2 ** i)
    
    B = bin(n - 1)[2:]
    result = 0
    l = len(B)
    for i in range (0, len(B)):
        if B[i] == "1":
            result = result + 2 ** (l - 1 - i) + L[l - 1 - i]
    
    print(result)
    L