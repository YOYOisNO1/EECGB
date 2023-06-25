def evklid(a, b):
        while b > 0:
            a, b = b, a % b
        return a
    
    t, w, b = tuple(map(int, input().split()))
    x = min(w, b)
    y = max(w, b)
    
    m = (x) * (t // (w * b // evklid(w, b)) + 1) - 1
    print(str(m // evklid(m, t)) + '/' + str(t // evklid(m, t)))    