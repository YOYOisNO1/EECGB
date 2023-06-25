def program802():
    """
    problem : https://codeforces.com/problemset/problem/452/A
    auther  : Jay Saha
    handel : ponder_
    date : 15/07/2020
    """
    
    pokemons = ['vaporeon', 'jolteon', 'flareon', 'espeon', 'umbreon', 'leafeon', 'glaceon', 'sylveon']
    n = int(input())
    maskedPM = input()
    
    for p in pokemons:
        if n == len(p):
            isValid = True
            for i in range(n):
                if maskedPM[i] != '.':
                    if maskedPM[i] != p[i]:
                        isValid = False
            if isValid:
                print(p)
                break