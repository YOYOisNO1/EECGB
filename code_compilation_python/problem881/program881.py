def program881():
        a, b, c, d, e, f = [int(input()) for _ in range(6)]
         
        suits1 = min(a,d)
        suits2 = min(b,c,d)
         
        total = 0
        if e>f:
            total += suits1 * e
            total += min(suits2,d-suits1)*f if d-suits1 > 0 else 0
        else:
            total += suits2 * f
         
            total += min(suits1,d-suits2)*e if d-suits2 > 0 else 0
         
        print(total)