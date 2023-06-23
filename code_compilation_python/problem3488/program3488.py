def program3488():
    
    
    player_one = 'Ciel'
    player_two = 'Hanako'
    
    
    c100, c10 = map(int, input().split())
    
    full_moves = min([c100 // 2, c10 // 24])
    
    c100 -= full_moves * 2
    c10 -= full_moves * 24
    
    if c100 < 2:
        if 100 * c100 + 10 * c10 >= 220 and c10 >= 2:
            c10 -= (220 - 100 * c100) // 10
            c100 = 0
        else:
            print(player_two)
            solved = True
    
        if not solved:
            if (c10 // 22) % 2 == 1:
                print(player_two)
            else:
                print(player_one)
    
    else:
        while True:
            if 100 * c100 + 10 * c10 >= 220 and c10 >= 2:
                tmp = min([2, c100])
                c100 -= tmp
                c10 -= (220 - 100 * tmp) // 10
            else:
                print(player_two)
                break
    
            if 100 * c100 + 10 * c10 >= 220 and c10 >= 2:
                if c10 >= 22:
                    c10 -= 22
                elif c10 >= 12:
                    c10 -= 12
                    c100 -= 1
                else:
                    c10 -= 2
                    c100 -= 2
            else:
                print(player_one)
                break
    
    
    
    
    
    
    