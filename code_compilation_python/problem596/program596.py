def program596():
    n = input()
    Min, Max = 999999999999999999L, -1
    
    i = 1
    while i * i <= n:
        if n % i == 0:
            n1 = n / i
            a = i + 1
    
            j = 1
            while j * j <= n1:
                if n1 % j == 0:
                    b = j + 2
                    c = n1 / j + 2
                    tmp = a * b * c - n
                    Min = min(tmp,Min)
                    Max = max(tmp,Max)
                j += 1
    
            a = n1 + 1
            j = 1
            while j * j <= i:
                if i % j == 0:
                    b = j + 2
                    c = i / j + 2
                    tmp = a * b * c - n
                    Min = min(tmp,Min)
                    Max = max(tmp,Max)
                j += 1
        i += 1
    print Min, Max