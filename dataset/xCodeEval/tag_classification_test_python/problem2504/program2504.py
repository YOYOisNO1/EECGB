def favourite_number(a, b, c):
        if b - a == 0:
            return "YES"
        elif c == 0:
            return "NO"
        elif (b - a) % c != 0 or (b - a) * c < 0:
            return "NO"
        return "YES"
    
    
    A, B, C = [int(i) for i in input().split()]
    print(favourite_number(A, B, C))