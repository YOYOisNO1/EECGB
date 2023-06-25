def program4219():
    import math
    k, n, s, p = map(int, input().split())
    
    numberSheetNedds = math.ceil(n * 1.0 / (s * 1.0))
    numberPackNeed = math.ceil(numberSheetNedds * k * 1.0 / (p * 1.0))
    print(int(numberPackNeed))