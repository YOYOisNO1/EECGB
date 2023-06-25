def program4468():
    a,b = map(int,input().split())
    c = 0
    menor = min(a,b)
    maior = max(a,b)
    if maior == menor == 1: print(0)
    else:
        while True:
            if maior == 0 or menor == 0: break
            maior -= 2
            menor += 1
            if maior < 3: maior, menor = menor, maior
            c += 1
        print(c) 