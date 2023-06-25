def program4218():
    import math
    
    k, n, s, p = map(int, input().split(" "))
    
    per_person_sheet = int(math.ceil(float(n) / s))
    
    print(int(math.ceil(float(k*per_person_sheet)) / p))