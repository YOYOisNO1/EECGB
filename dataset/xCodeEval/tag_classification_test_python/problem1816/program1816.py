def program1816():
    
    A = (len(input().split('.')[1]), 'A')
    B = (len(input().split('.')[1]), 'B')
    C = (len(input().split('.')[1]), 'C')
    D = (len(input().split('.')[1]), 'D')
    
    tab = sorted([A, B, C, D])
    
    if tab[0][0] * 2 <= tab[1][0] and tab[-1][0] < tab[-2][0] * 2:
        print(tab[0][1])
    elif tab[-1][0] >= tab[-2][0] * 2 and tab[0][0] * 2 > tab[1][0]:
        print(tab[-1][1])
    else:
        print('C')
    
    
    