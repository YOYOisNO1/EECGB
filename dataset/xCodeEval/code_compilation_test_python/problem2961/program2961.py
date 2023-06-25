def program2961():
    import math
    n, m = map(int, input().split())
    
    if m >= n:
        print(n)
    else:
        disc = 1 + 8 * (n - m)
        dr = (-1 + pow(disc, 0.5)) / 2.0
        dr = math.ceil(dr);
        if (dr * (dr - 1) >= 2 * (n - m)) {
            dr -= 1
        }
        if (dr * (dr + 1) < 2 * (n - m)) {
            dr += 1
        }
        print(m + dr)