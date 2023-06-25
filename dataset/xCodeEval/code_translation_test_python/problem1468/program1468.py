def nod(a, b):
        if(b == 0): return a
        else: return nod(b, a % b)
    
    n = input()
    s = 0
    col = n - 2
    for i in range(2, n):
        os = []
        k = n
        while k > 0:
            os.append(k % i)
            k /= i
        s += sum(os)
    x = nod(s, col)
    print(str(s / x) + '/' + str(col / x))