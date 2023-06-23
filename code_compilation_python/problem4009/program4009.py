    import math
    
def f(t):
        return math.sqrt(abs(t)) + 5 * t ** 3
    
    a = [float(input()) for _ in range(11)]
    for i, t in reversed(list(enumerate(a))):
        y = f(t)
        if y > 400:
            print('f(' + i + ') = MAGNA NIMIS!')
        else:
            print('f(' + i + ') =', '{:.2f}'.format(y))