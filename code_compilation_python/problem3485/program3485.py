def program3485():
    m100, m10 = input().split(' ')
    
    m100 = int(m100)
    m10 = int(m10)
    
    turn_no = 1
    
    while True:
        if turn_no % 2: # Ceil
            if m100 >= 2:
                if m10 >= 2:
                    m100 -= 2
                    m10 -= 2
                else:
                    break
            elif m100 == 1:
                if m10 >= 12:
                    m100 -= 1
                    m10 -= 12
                else:
                    break
            else:
                if m10 >= 22:
                    m10 -= 22
                else:
                    break
        else: # Hanako
            if m10 >= 22:
                m10 -= 22
            elif m10 >= 12:
                if m100 >= 1:
                    m100 -= 1
                    m10 -= 12
                else:
                    break
            elif m10 >= 2:
                if m100 >= 2:
                    m100 -= 2
                    m10 -= 2
                else:
                    break
            else:
                break
    
        turn_no += 1
    
    if turn_no % 2:
        print 'Hanako'
    else:
        print 'Ciel'
    
    
    
    