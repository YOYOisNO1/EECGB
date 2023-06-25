def program2178():
    from itertools import accumulate
    
    n, c = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    t = [int(x) for x in input().split()]
    t_p = list(accumulate(t))
    t_s = list(accumulate(reversed(t)))
    Limak = sum(max(0, p[i] - c * t_p[i]) for i in range(n))
    Radewoosh = sum(max(0, p[n-1-i] - c * t_s[i]) for i in range(n))
    if Limak > Radewoosh:
        print('Limak')
    elif Limak < Radewoosh:
        print('Radewoosh')
    else:
        print('Tie')