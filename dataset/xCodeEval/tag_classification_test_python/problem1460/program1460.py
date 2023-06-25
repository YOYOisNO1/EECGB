def program1460():
    a, b = (int(input().replace(' ', ''), 2) for _ in' '*2)
    print('YNEOS'[a ^ b == 7::2])