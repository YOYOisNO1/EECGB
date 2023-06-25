    tc = input()
    card1, card2 = input().split()
    card1suit = card1[1]
    card2suit = card2[1]
    card1val = card1[0]
    card2val = card2[0]
    
    if card1suit == tc and card2suit != tc:
        print('YES')
        exit()
def rank_val(s):
        if s == '6' or s == '7' or s == '8' or s == '9':
            return int(s)
        elif s == 'T':
            return 10
        elif s == 'J':
            return 11
        elif s == 'Q':
            return 12
        elif s == 'K':
            return 13
        elif s == 'A':
            return 14
    
    if card1suit == card2suit:
        if rank_val(card1val) > rank_val(card2val):
            print('YES')
            exit()
        else:
            print('NO')
            exit()
    print('NO')